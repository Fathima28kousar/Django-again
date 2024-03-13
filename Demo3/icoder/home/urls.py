from django.urls import path
from home.views import *

urlpatterns =[
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('search/',search,name='search'),
]