from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from GARAGE_APP.models import Login, Service, Customer, Car, Availability, ServiceStatus, Booking


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)


    class Meta:
             model = Login
             fields = ('username', 'password1', 'password2')

class ServiceRegister(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'address', 'phone', 'email', 'opening_time','closing_time','document')


class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'phone','document')



class CarRegister(forms.ModelForm):
    class Meta:
        model = Car
        fields =('model','number_plate','rc_number', 'car_name', 'brand','model','year_of_manufacture','fuel_type','registration_number','type','document')


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ('date', 'start_time','end_time','is_available')

class ServiceStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceStatus
        fields = ('car_details','choice', 'date','time')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('status',)


