from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_sermon, name='latest_sermon'),  # Use 'latest_sermon' as the name
    path('add/', views.add_sermon, name='add_sermon'),
    path('sermon/edit/<int:pk>/', views.edit_sermon, name='edit_sermon'),
    path('sermon/delete/<int:pk>/', views.delete_sermon, name='delete_sermon'),
]
