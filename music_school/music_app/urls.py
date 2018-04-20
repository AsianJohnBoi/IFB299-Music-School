from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('reg_form/', views.reg_form, name='reg_form'),
    path('bookings/', views.bookings, name='bookings'),
    path('lessons/', views.lessons, name='lessons'),
    path('admin/', admin.site.urls),    
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('account/', views.account, name='account'),
    path('account/login/', views.account, name='login'),   
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp, name='signup'),
    path('account/edit/', views.edit_account, name='edit_account')
]
