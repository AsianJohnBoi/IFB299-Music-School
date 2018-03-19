from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('reg_from/', views.reg_form, name='reg_form')

]
