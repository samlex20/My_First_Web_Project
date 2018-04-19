
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

# Create your views here.



def post_list(request):#This fxn takes a request
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})#This fxn puts together our template blog/post_list.html
#in the render fxn
#parameter request, picks all requests from the internet user.
#parameter 'blog/post_list.html' gives the template.
#parameter{} we add somethings for the template to use.
#{'posts': posts}. Please note that the part before : is a string; you need to wrap it with quotes: ''

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST,) # create a new Post form, we need to call PostForm()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form}) #pass the form to the template.



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
