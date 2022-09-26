from django.contrib import admin
from django.urls import path

from . import views
urlpatterns=[
    path('',views.home),
    path('profile',views.profile),
    path('event',views.event),
    path('login',views.login),
    path('signup',views.signup),
]