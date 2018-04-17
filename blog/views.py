from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.



def post_list(request):#This fxn takes a request
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})#This fxn puts together our template blog/post_list.html

#in the render fxn
#parameter request, picks all requests from the internet user.
#parameter 'blog/post_list.html' gives the template.
#parameter{} we add somethings for the template to use.
#{'posts': posts}. Please note that the part before : is a string; you need to wrap it with quotes: ''
