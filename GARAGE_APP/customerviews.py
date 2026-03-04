from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from GARAGE_APP.forms import CustomerRegister, CarRegister
from GARAGE_APP.models import Customer, Service, Availability, Car, ServiceStatus, Booking
from GARAGE_APP.views import customer


def customer_profile(request):
    data=request.user
    customer_profile = Customer.objects.get(customer_details=data.id)
    return render(request,"customer/customer_profile.html",{'data':customer_profile})

def customer_edit(request):

    user = request.user
    customer=Customer.objects.get(customer_details=user)

    if request.method=='POST':
        customer_form =CustomerRegister(request.POST,request.FILES, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer_profile')
    else:
        customer_form = CustomerRegister(instance=customer)
    return render(request, "customer/customer_edit.html", {"data":customer_form})

# ------------------------------------------------------------------------------
def customer_list(request):
    data=Customer.objects.filter(customer_details=request.user)
    return render(request,'customer/customer_list.html',{'data':data})


def customer_update(request, id):
    customer_update = Customer.objects.get(id=id)
    if request.method == "POST":
        customer_form = CustomerRegister(request.POST, request.FILES, instance=customer_update)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer_list')

    else:
        customer_form = CustomerRegister(instance=customer_update)
    return render(request, 'customer/customer_update.html', {'customer_form': customer_form})


def customer_delete(request,id):
    customer_delete=Customer.objects.get(id=id)
    customer_delete.delete()
    return redirect('customer_list')


def car_add(request):
    if request.method == "POST":
        car_form = CarRegister(request.POST, request.FILES)

        if car_form.is_valid():
            car = car_form.save(commit=False)

            try:
                customer = Customer.objects.get(customer_details=request.user)
            except Customer.DoesNotExist:
                return render(request, "customer/car_add.html", {
                    "car_form": car_form,
                    "error": "Customer profile not found"
                })

            car.car_details = customer
            car.save()

            return redirect("car_view")

    else:
            car_form = CarRegister()

    return render(request, "customer/car_add.html", {"car_form": car_form})


def car_view(request):
    customer = Customer.objects.get(customer_details=request.user)
    data = Car.objects.filter(car_details=customer)
    return render(request, "customer/car_view.html", {"data": data,})



def car_update(request, id):
    car_update = Car.objects.get(id=id)
    if request.method == "POST":
        car_form = CarRegister(request.POST, request.FILES, instance=car_update)
        if car_form.is_valid():
            car_form.save()
        return redirect('car_view')
    else:
        car_form = CarRegister(instance=car_update)
        return render(request, "customer/car_update.html", { "car_form": car_form,})


def car_delete(request, id):
    car_delete = Car.objects.get(id=id)
    car_delete.delete()
    return redirect('car_view')


def view_availability(request):
    data = Availability.objects.all()
    return render(request, 'customer/view_availability.html',{"data":data})

def status_views(request):
    data=ServiceStatus.objects.all()
    return render(request, "customer/status_views.html", {"data":data})






def book_now(request, id):

    if not request.user.is_authenticated:
        return redirect("login")

    availability = Availability.objects.filter(id=id).first()

    if not availability:
        return redirect("view_availability")

    customer = Customer.objects.filter(
        customer_details=request.user
    ).first()

    if customer and availability.is_available:

        Booking.objects.create(
            availability=availability,
            customer=customer,
            status="pending"
        )

        availability.is_available = False
        availability.save()

    return redirect("booking_view")

def booking_view(request):
    bookings = Booking.objects.filter(customer__customer_details=request.user)
    return render(request, "customer/booking_view.html", { "data": bookings})



def Log_out(request):
    logout(request)
    return redirect('index')