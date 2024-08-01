from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def add_bank(request):
    # view logic here
    return render(request, 'add_bank.html')
def add_branch(request):
    # view logic here
    return render(request, 'add_branch.html')
def list_banks(request):
    # view logic here
    return render(request, 'list_banks.html')
def bank_detail(request):
    # view logic here
    return render(request, 'bank_detail.html')
def branch_detail(request):
    # view logic here
    return render(request, 'branch_detail.html')
def edit_branch(request):
    # view logic here
    return render(request, 'edit_branch.html')