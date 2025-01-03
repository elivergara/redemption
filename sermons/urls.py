from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_sermon, name='sermons'),
    path('add/', views.add_sermon, name='add_sermon'),
]
