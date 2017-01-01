from django import forms
from .models import Poster


class PosterForm(forms.ModelForm):
	info = forms.CharField(widget=forms.Textarea(attrs={
				'placeholder' : "Write instructions here...", 
				'style' : 'padding: 10px; padding-top: 15px;' ,
				'class' : 'form-control'
			}), label='')
	class Meta:
		model = Poster
		fields = ('info', )

class PosterEditForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={
				'placeholder' : 'Title',
				'style' : 'width:100%',
				'class' : 'char-field'
		}), label='')
	image = forms.CharField(widget=forms.TextInput(attrs={
				'placeholder' : 'Image',
				'style' : 'width:100%',
				'class' : 'char-field'
		}), label='')
	year = forms.CharField(widget=forms.TextInput(attrs={
				'placeholder' : 'Year',
				'style' : 'width:100%',
				'class' : 'char-field'
		}), label='')
	genre = forms.CharField(widget=forms.TextInput(attrs={
				'placeholder' : 'Genre',
				'style' : 'width:100%',
				'class' : 'char-field'
		}), label='')

	class Meta:
		model = Poster
		fields = '__all__'
