from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('extract/', views.extract, name='extract'),
    path('result/', views.result, name='result'),
    path('example/', views.example, name='example'),
]