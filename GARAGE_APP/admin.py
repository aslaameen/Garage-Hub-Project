from django.contrib import admin

from GARAGE_APP import models

# Register your models here.

admin.site.register(models.Login)
admin.site.register(models.Service)
admin.site.register(models.Customer)
admin.site.register(models.Car)
admin.site.register(models.Booking)
