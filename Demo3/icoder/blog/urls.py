from django.urls import path
from blog.views import *

urlpatterns = [
    path('postComment/',postComment,name='postComment'),
    path('',blogHome,name='blogHome'),
    path('<str:slug>/',blogPost, name="blogPost"),
]

