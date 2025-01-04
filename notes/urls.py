from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
]
