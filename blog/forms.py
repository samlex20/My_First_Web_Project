from django import forms  #imports django forms
from .models import Post  #imports our post model

class PostForm(forms.ModelForm): #PostForm = name of our Form  #forms.ModelForm ttells django this is a model form
	
	class Meta:   #tells django which model should be used to create the form

		model = Post

		fields = ('title', 'text',)    #we can say which field(s) should end up in our form
