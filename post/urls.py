from django.urls import path
import post.views

urlpatterns = [
    path('', post.views.index),
    path('posts/', post.views.get_posts, name='posts'),
]

