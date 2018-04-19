from django.conf.urls import url #imports djangos function url
from . import views #imports all of our views from the blog app
from django.urls import path, re_path



urlpatterns = [
    path('', views.post_list, name='post_list'), #assigns a view called post_list to '' url. tells django that views.post_list is the right place to go when a visitor visits the site
    #path('^$', views.post_list, name='post_list'),
    #name='post_list' can be the name of the url used to identify the view or name of view
    #path('post/(?P<int:pk>\d+)/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
