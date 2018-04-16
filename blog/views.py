from django.shortcuts import render

# Create your views here.



def post_list(request):#This fxn takes a request
	return render(request, 'blog/post_list.html', {})#This fxn puts together our template blog/post_list.html