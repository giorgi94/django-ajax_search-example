from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings

from .models import Poster
from .forms import PosterEditForm


def admin_log(request):
	admin = User.objects.all()[0]
	login(request,admin)
	return redirect('/admin')

def index(request):	
	all_poster = Poster.objects.all()
	query = request.GET.get('q')
	if query:
		all_poster = all_poster.filter(
					Q(genre__iregex=query) | 
					Q(title__iregex=query) |
					Q(year__iregex=query))

	paginator = Paginator(all_poster, 28)

	page = request.GET.get('page')
	try:
		poster_list = paginator.page(page)
	except PageNotAnInteger:
		poster_list = paginator.page(1)
	except EmptyPage:
		poster_list = paginator.page(paginator.num_pages)


	context = {
		'all_poster' : all_poster,
		'poster_list' : poster_list
	}
	return render(request, 'index.html', context)


def detail(request, poster_id):	
	poster = get_object_or_404(Poster, id=poster_id)

	context = {
		'poster' : poster
	}
	return render(request, 'detail.html', context)



def add_poster(request):
	form = PosterEditForm()
	if request.method == "POST":
		poster = Poster()
		poster.title = request.POST.get('title')
		poster.image = request.POST.get('image')
		poster.year = request.POST.get('year')
		poster.genre = request.POST.get('genre')
		poster.save()
		return redirect(reverse('poster:detail', kwargs={"poster_id": poster.id}))

	context = {
		'form' : form
	}
	return render(request, 'addvideo.html', context)

def edit(request, poster_id):
	poster = get_object_or_404(Poster, id=poster_id)

	if request.method == "POST":
		poster.title = request.POST.get('title')
		poster.image = request.POST.get('image')
		poster.year = request.POST.get('year')
		poster.genre = request.POST.get('genre')
		poster.save()
		return redirect(reverse('poster:detail', kwargs={"poster_id": poster_id}))

	form = PosterEditForm(initial={
			'title' : poster.title,
			'image': poster.image,
			'year': poster.year,
			'genre':  poster.genre
		})

	context = {
		'poster' : poster,
		'form' : form
	}
	return render(request, 'editvideo.html', context)




def search(request):
	if request.method == "POST":
		search = request.POST.get('search')	

		posters = Poster.objects.filter(
					Q(genre__iregex=search) | 
					Q(title__iregex=search) |
					Q(year__iregex=search))

		if len(search)==0: 
			posters = []	


		return render(request, 'ajax_search/search.html', { 'posters' : posters })
	raise Http404