from django.urls import path
from .views import add_bank, add_branch, list_banks, bank_detail, branch_detail, edit_branch

urlpatterns = [
    path('add-bank/', add_bank, name='add_bank'),
    path('add-branch/<int:bank_id>/', add_branch, name='add_branch'),
    path('banks/', list_banks, name='list_banks'),
    path('bank/<int:bank_id>/', bank_detail, name='bank_detail'),
    path('branch/<int:branch_id>/', branch_detail, name='branch_detail'),
    path('edit-branch/<int:branch_id>/', edit_branch, name='edit_branch'),
]
