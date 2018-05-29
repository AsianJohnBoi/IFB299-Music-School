"""
Specifies the path of each page, when clicking on a link, will redirect user. Calls functions in views.py to
render the html page and display to the user.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

#The URL paths/patterns
urlpatterns = [
    path('', views.indexPage, name='index'),
    path('about/', views.aboutPage, name='about'),
    path('services/', views.servicesPage, name='services'),
    path('contact/', views.contactPage, name='contact'),
    path('pricing/', views.pricingPage, name='pricing'),
    path('reg_form/', views.reg_formPage, name='reg_form'),
    path('bookings/', views.bookingsPage, name='bookings'), #displays all available lessons teaching any instrument
    path('bookings_Piano/', views.bookings_Piano, name='bookings_Piano'), #displays lessons for Piano
    path('bookings_Saxophone/', views.bookings_Saxophone, name='bookings_Saxophone'), #displays lessons for Claranet
    path('bookings_Flute/', views.bookings_Flute, name='bookings_Flute'), #displays lessons for flute
    path('bookings_Violin/', views.bookings_Violin, name='bookings_Violin'), #displays lessons for Violin
    path('bookings_Guitar/', views.bookings_Guitar, name='bookings_Guitar'), #displays lessons for Guitar
    path('bookings_Drums/', views.bookings_Drums, name='bookings_Drums'), #displays lessons for Trumpet
    path('bookings_English/', views.bookings_English, name='bookings_English'),
    path('bookings_Spanish/', views.bookings_Spanish, name='bookings_Spanish'),
    path('bookings_Italian/', views.bookings_Italian, name='bookings_Italian'),
    path('bookings_German/', views.bookings_German, name='bookings_German'),
    path('bookings_Chinese/', views.bookings_Chinese, name='bookings_Chinese'),
    path('bookings_French/', views.bookings_French, name='bookings_French'),
    path('lessons/', views.lessonsPage, name='lessons'),
    path('instrument/', views.instrumentPage, name='instrument'),  
    path('payment/', views.paymentPage, name='payment'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('account/', views.accountPage, name='account'),
    path('account/login/', views.accountPage, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpPage, name='signup'),
    path('account/edit/', views.edit_accountPage, name='edit_account'),
]
