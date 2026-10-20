from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from accounts.forms import *


def register_page(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Your account has been created successfully.'
            )

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_page(request):

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                f'Welcome back, {user.username}!'
            )

            return redirect('home')

    else:
        form = LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def logout_page(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out successfully.'
    )

    return redirect('login')