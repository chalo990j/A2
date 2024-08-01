from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import JsonResponse, HttpResponse

def login_view(request):
    return render(request, 'login.html')
def home_view(request):
    return render(request, 'home.html')
def register_view(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is invalid'})
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
def profile(request):
    # Your profile logic here
    return render(request, 'accounts/profile.html')

@login_required
def profile_view(request):
    user = request.user
    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return JsonResponse(data)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password1 and password1 == password2:
            user.set_password(password1)
        user.save()
        return redirect('profile')
    return render(request, 'accounts/edit_profile.html')
