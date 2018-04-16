from django.conf.urls import url #imports djangos function url
from . import views #imports all of our views from the blog app
from django.urls import path



urlpatterns = [
    path('', views.post_list, name='post_list'), #assigns a view called post_list to '' url. tells django that views.post_list is the right place to go when a visitor visits the site
    #path('^$', views.post_list, name='post_list'),
    #name='post_list' can be the name of the url used to identify the view or name of view
]
