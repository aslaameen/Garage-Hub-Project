from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from GARAGE_APP.forms import ServiceRegister, CarRegister, AvailabilityForm, ServiceStatusForm, BookingForm
from GARAGE_APP.models import Service, Car, Login, Customer, Availability, ServiceStatus, Booking
from GARAGE_APP.views import customer


def service_profile(request):
    data=request.user
    service_profile = Service.objects.get(service_details=data.id)
    return render(request,"service_center/service_profile.html",{'data':service_profile})



def profile_edit(request):

    user = request.user
    service=Service.objects.get(service_details=user)

    if request.method=='POST':
        service_form =ServiceRegister(request.POST,request.FILES, instance=service)
        if service_form.is_valid():
            service_form.save()
            return redirect('service_profile')
    else:
        service_form = ServiceRegister(instance=service)
    return render(request, "service_center/profile_edit.html", {"data":service_form})
# ---------------------------------------------------------------------------------------
def service_list(request):
    data=Service.objects.all()
    return render(request,'service_center/service_list.html',{'data':data})


def service_update(request, id):
    serv_update = Service.objects.get(id=id)
    if request.method == "POST":
        serv_form = ServiceRegister(request.POST, request.FILES, instance=serv_update)
        if serv_form.is_valid():
            serv_form.save()
            return redirect('service_list')

    else:
        serv_form = ServiceRegister(instance=serv_update)
    return render(request, 'service_center/service_update.html', {'serv_form': serv_form})




def service_delete(request,id):
    service_delete=Service.objects.get(id=id)
    service_delete.delete()
    return redirect('service_list')



def car_list(request):
    data=Car.objects.all()
    return render(request, "service_center/car_list.html", {"data":data})



def availability_add(request):
    if request.method == 'POST':
        avl_form = AvailabilityForm(request.POST)
        if avl_form.is_valid():
            available = avl_form.save(commit=False)
            serv = Service.objects.get(service_details=request.user)
            available.service = serv
            available.save()
            return redirect('available_list')
    else:
        avl_form = AvailabilityForm()
    return render(request, "service_center/availability_add.html", {"data":avl_form})

def available_list(request):
    data=Availability.objects.all
    return render(request, "service_center/available_list.html", {"data":data})

def available_update(request, id):
    avl_update = Availability.objects.get(id=id)
    if request.method == "POST":
        avl_form = AvailabilityForm(request.POST, request.FILES, instance=avl_update)
        if avl_form.is_valid():
            avl_form.save()
            return redirect('available_list')

    else:
        avl_form = AvailabilityForm(instance=avl_update)
    return render(request, 'service_center/available_update.html', {'avl_form': avl_form})


def available_delete(request,id):
    avl_delete=Availability.objects.get(id=id)
    avl_delete.delete()
    return redirect('available_list')



def status_add(request):
    if request.method == 'POST':
         status_form = ServiceStatusForm(request.POST)
         if status_form.is_valid():
            status = status_form.save(commit=False)
            serv = Service.objects.get(service_details=request.user)
            status.service = serv
            status.save()
         return redirect('status_view')
    else:
            status_form = ServiceStatusForm()
    return render(request, "service_center/status_add.html", {"data":status_form})

def status_view(request):
    data=ServiceStatus.objects.all()
    return render(request, "service_center/status_view.html", {"data":data})



def status_update(request, id):
    status_update = ServiceStatus.objects.get(id=id)
    if request.method == "POST":
        status_form = ServiceStatusForm(request.POST, request.FILES, instance=status_update)
        if status_form.is_valid():
            status_form.save()
            return redirect('status_view')

    else:
        status_form = ServiceStatusForm(instance=status_update)
    return render(request, 'service_center/status_update.html', {'status_form': status_form})


def status_delete(request,id):
    status_delete=ServiceStatus.objects.get(id=id)
    status_delete.delete()
    return redirect('status_view')



def all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, "service_center/all_bookings.html", { "data": bookings})

def booking_status(request, id):

    booking = Booking.objects.get(id=id)

    if request.method == "POST":
        booking.status = request.POST.get("status")
        booking.save()
        return redirect('all_bookings')

    return render(request, "service_center/booking_status.html", {"booking": booking})




def Log_out(request):
    logout(request)
    return redirect('index')