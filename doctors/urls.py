from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('appointment', views.appointment_view, name='appointment'),
    path('doctors', views.all_doctors, name='doctors'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]