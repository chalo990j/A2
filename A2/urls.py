"""
URL configuration for A2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import home, add_bank, add_branch, list_banks, bank_detail, branch_detail, edit_branch

urlpatterns = [
    path('', home, name='home'),
     path('accounts/', include('accounts.urls', namespace='accounts')), 

    path('add-bank/', add_bank, name='add_bank'),
    path('add-branch/<int:bank_id>/', add_branch, name='add_branch'),
    path('banks/', list_banks, name='list_banks'),
    path('bank/<int:bank_id>/', bank_detail, name='bank_detail'),
    path('branch/<int:branch_id>/', branch_detail, name='branch_detail'),
    path('edit-branch/<int:branch_id>/', edit_branch, name='edit_branch'),
]


