from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
     path('profile/', views.profile, name='profile'),
    path('profile/view/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='edit_profile'),
]
