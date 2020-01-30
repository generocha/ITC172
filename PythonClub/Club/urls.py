from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resources/', views.gettypes, name='resources'),
]
