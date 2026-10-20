from django.shortcuts import render, redirect

# Create your views here.

def home_page(request):
    return render(request, 'main/home.html')

def about_page(request):
    return render(request, 'main/about.html')

def contact_page(request):
    return render(request, 'main/contact.html')
