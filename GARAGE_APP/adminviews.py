from django.contrib.auth import logout
from django.shortcuts import render, redirect

from GARAGE_APP.models import Customer, Availability, Car, ServiceStatus, Service, Booking


def customers_list(request):
    data=Customer.objects.all()
    return render(request,'admin/customers_list.html',{'data':data})


def car_views(request):
    data = Car.objects.all()
    return render(request, "admin/car_views.html", {"data": data})


def availability_views(request):
    data = Availability.objects.all()
    return render(request, 'admin/availability_views.html',{"data":data})


def view_status(request):
    data=ServiceStatus.objects.all()
    return render(request, "admin/view_status.html", {"data":data})


def service_lists(request):
    data=Service.objects.all()
    return render(request,'admin/service_lists.html',{'data':data})


def all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, "admin/all_bookingss.html", { "data": bookings})

def booking_statuss(request, id):

    booking = Booking.objects.get(id=id)

    if request.method == "POST":
        booking.status = request.POST.get("status")
        booking.save()
        return redirect('all_bookingss')

    return render(request, "admin/booking_statuss.html", {"booking": booking})








def Log_out(request):
    logout(request)
    return redirect('index')












