from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import Model


class Login(AbstractUser):
    is_service = models.BooleanField(default=False)
    is_customer= models.BooleanField(default=False)


class Service(models.Model):
    service_details = models.OneToOneField('Login', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_details = models.OneToOneField('Login', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.name



class Car(models.Model):
    car_details = models.ForeignKey("Customer", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    rc_number = models.CharField(max_length=20)
    car_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year_of_manufacture = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)

    service_type = (
        ("BASIC CAR CHECKS", " basic car checks"),
        ("FULL SERVICE", "full service"),
        ("MAJOR SERVICE", "major service"),
        ("MANUFACTURER SERVICE", "manufacturer service"),
        ("INTERIM SERVICE", "interim service"),

    )
    type = models.CharField(max_length=100,
                            choices=service_type,
                            default="BASIC CAR CHECKS")

    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.number_plate




class Availability(models.Model):
    service = models.ForeignKey("Service", on_delete=models.DO_NOTHING)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)





class ServiceStatus(models.Model):
    car_details = models.ForeignKey("Car", on_delete=models.CASCADE)
    status_choice = (
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("WAITING_PARTS", "Waiting Parts"),
        ("COMPLETED", "Completed"),
        ("CANCELED", "Canceled"),
    )
    choice = models.CharField(max_length=100,
                              choices=status_choice,
                              default="PENDING")
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.car_details


class Booking(models.Model):
    availability = models.ForeignKey("Availability", on_delete=models.DO_NOTHING)
    customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('slot not available', 'Slot Not Available'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')





