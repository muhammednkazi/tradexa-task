# in this file we handle the urls

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('blogs',views.blogs,name="blogs"),
    path('addpost',views.addpost,name="addpost"),
    path('blogpost/<int:id>',views.blogpost,name="blogpost")
]
