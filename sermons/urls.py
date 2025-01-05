from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_sermon, name='latest_sermon'),  # Use 'latest_sermon' as the name
    path('add/', views.add_sermon, name='add_sermon'),
]
