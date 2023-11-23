from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
# import requests
# from django.http import HttpResponse

from .models import CustomUser
from .forms import SignupForm, LoginForm


# On the homepage, users can view the documentation of the API, plus links to view their API key.
def homepage(request):
    return render(request, 'homepage.html')

      
# There will be a page here, which will show the API key(s) to the user when they visit.
@login_required
def dashboard(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    api_key = request.user.api_key
    api_key_status = request.user.api_key_status
    
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'api_key': api_key,
        'api_key_status': api_key_status,
    }
    
    return render(request, 'dashboard.html', context)


# A 16-characters unique API key is generated.
def generate_unique_api_key():
    while True:
        api_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        if not CustomUser.objects.filter(api_key=api_key).exists():
            return api_key
        
        
# The API key is generated for every user upon successful signup     
@receiver(post_save, sender=CustomUser)
def generate_key_on_signup(sender, instance, created, **kwargs):
    if created:
        instance.api_key = generate_unique_api_key()
        instance.save()
        
        

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = CustomUser(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(form.cleaned_data['password'])
            user.api_key = generate_unique_api_key() # Here, we call the function we defined earlier to generate the API key for the newly registered user.
            user.save()
            
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')



@login_required
def delete_account(request):
    user = request.user
    user.delete()
    return redirect('signup')