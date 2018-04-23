from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, authenticate, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from music_app.forms import SignUpForm, EditProfileForm

def login(request):
    return render(request, 'registration/login.html')

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

def reg_form(request):
    return render(request, 'music_app/reg_form.html')

def bookings(request):
    return render(request, 'music_app/bookings.html')

def dashboard(request):
    return render(request, 'music_app/dashboard.html')

def lessons(request):
    return render(request, 'music_app/lessons.html')

def account(request):
    return render(request, 'music_app/account.html')

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('../account/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def edit_account(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/music_app/account/')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'music_app/edit_account.html', {'form' : form})
