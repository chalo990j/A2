from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from .forms import BankForm, BranchForm
from .models import Bank, Branch

@login_required
def add_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.save()
            return redirect('bank_detail', bank_id=bank.id)
    else:
        form = BankForm()
    return render(request, 'banks/add_bank.html', {'form': form})

@login_required
def add_branch(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    if bank.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank
            branch.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm()
    return render(request, 'banks/add_branch.html', {'form': form, 'bank': bank})

def list_banks(request):
    banks = Bank.objects.all()
    return render(request, 'banks/list_banks.html', {'banks': banks})
def list_banks(request):
    # Your logic to get the list of banks
    return render(request, 'list_banks.html')
def bank_detail(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    branches = bank.branches.all()
    return render(request, 'banks/bank_detail.html', {'bank': bank, 'branches': branches})

def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    data = {
        'id': branch.id,
        'name': branch.name,
        'transit_number': branch.transit_number,
        'address': branch.address,
        'email': branch.email,
        'capacity': branch.capacity,
        'last_modified': branch.last_modified,
    }
    return JsonResponse(data)

@login_required
def edit_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if branch.bank.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)
    return render(request, 'banks/edit_branch.html', {'form': form})
