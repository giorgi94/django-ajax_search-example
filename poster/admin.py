from django.contrib import admin
from .models import Poster

class PosterAdmin(admin.ModelAdmin):
	list_display =  ['title', 'genre' ,'year']
	search_fields = ['title', 'genre' , 'year', 'image'] 

	class Meta:
		model = Poster

admin.site.register(Poster, PosterAdmin)
