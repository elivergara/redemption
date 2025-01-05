from django.urls import path
from . import views

urlpatterns = [
 
    path('latest/', views.latest_sermon, name='latest_sermon'),
    path('add/', views.add_sermon, name='add_sermon'),
]
