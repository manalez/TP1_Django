from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib import messages  # Assurez-vous d'importer messages
from .forms import LoginForm  # Ajoutez cette ligne



def welcome_view(request, username):
    return render(request, 'welcome.html', {'username': username})


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f'User {username} has logged in successfully.')
                return redirect(f'/accounts/welcome/{user.username}/')  # Ajoutez /accounts/ ici
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe invalide!')
                print('Login failed: Invalid credentials.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})