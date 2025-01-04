from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),  # Your profile page
    path('', views.index, name='index'),  # Homepage
    path('update-subscription/', views.update_subscription, name='update_subscription'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='home/password_change.html'), 
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='home/password_change_done.html'), 
         name='password_change_done'), 
    path('events/', views.events_list, name='events'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


