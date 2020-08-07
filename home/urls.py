from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.show_chart, name='chart'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
