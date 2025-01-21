from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_news, name='add_news'),
    path('', views.news_list, name='news'),
    path('edit/<int:pk>/', views.edit_news, name='edit_news'),
    path('delete/<int:pk>/', views.delete_news, name='delete_news'),
]
