from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('singup/', views.singup, name="singup"),
    path('singin/', views.singin, name="singin"),
    path('singout/', views.singout, name="singout"),
]
