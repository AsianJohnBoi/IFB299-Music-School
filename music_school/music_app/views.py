from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'music_app/index.html')

def about(request):
    return render(request, 'music_app/about.html')

def services(request):
    return render(request, 'music_app/services.html')

def contact(request):
    return render(request, 'music_app/contact.html')

def pricing(request):
    return render(request, 'music_app/pricing.html')
