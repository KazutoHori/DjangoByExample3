from django.urls import path
from . import views

app_name = 'contents'
urlpatterns = [
    path('create/', views.content_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.content_detail, name='detail'),
    path('like/', views.content_like, name='like'),

    path('', views.content_list, name='list'),
    path('ranking/', views.content_ranking, name='ranking'),
]
