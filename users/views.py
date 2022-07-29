from multiprocessing import reduction
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('tasks')

        
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        # print('HELLO')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.capitalize()
            user.save()
            login(request, user)
            messages.success(request, 'User was successfully created.')
            return redirect('tasks')

    context = {'form': form}
    return render(request, 'users/register-user.html', context)            

def loginUser(request):
    # form = LoginForm()
    if request.user.is_authenticated:
        return redirect('tasks')

    if request.method == 'POST':
        username = request.POST.get('username').capitalize()
        password = request.POST.get('password')

        # try:
        #     user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'User was logged in.')
            return redirect('tasks')
        else:
            # print("Password or Username is incorrect...") 
            messages.error(request, 'Password or Username is incorrect...')
            return redirect('login')


    context ={}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'The user was logged out.')

    return redirect('home')