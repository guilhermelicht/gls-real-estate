from django.urls import path 
from . import views

urlpatterns = [
    # 1st arg: route. here we don't use '/'
    # 2nd arg: method (need to create the index inside views)
    # 3rd arg: the name to access
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]