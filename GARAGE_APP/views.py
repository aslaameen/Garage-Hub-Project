from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from GARAGE_APP.forms import ServiceRegister, LoginRegister, CustomerRegister


# Create your views here.


def index(request):
    return render (request,'index.html')

def dash(request):
    return render(request,'dash.html')




#        base views
# ---------------------------




def admin_home(request):
    return render(request,'admin/adminbase.html')

def service_center(request):
    return render(request,'service_center/service_centerbase.html')

def customer(request):
    return render(request,'customer/customerbase.html')

#        base views
# ---------------------------

def login_view(request):
    if request.method == "POST":
         username = request.POST.get('uname')
         password = request.POST.get('pass')

         user = authenticate(request, username=username, password=password)
         # authenticate= inbuild function aan
         if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect ('admin_home')
            elif user.is_service:
                return redirect('service_center')
            elif user.is_customer:
                return redirect('customer')
         else:
             messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')



def service_add(request):

    if request.method == "POST":
        service_form = ServiceRegister(request.POST,request.FILES,request.FILES)
        login_form = LoginRegister(request.POST)



        if service_form.is_valid() and login_form.is_valid():
            service=login_form.save(commit=False)
            service.is_service=True
            service.save()

            user = service_form.save(commit=False)
            user.service_details = service
            user.save()

    else:
        service_form=ServiceRegister()
        login_form = LoginRegister()
    return render(request,'register.html',{'service_form':service_form,'login_form':login_form})


def customer_add(request):

    if request.method == "POST":
        customer_form = CustomerRegister(request.POST,request.FILES,request.FILES)
        login_form = LoginRegister(request.POST)



        if customer_form.is_valid() and login_form.is_valid():
            cust=login_form.save(commit=False)
            cust.is_customer=True
            cust.save()

            user= customer_form.save(commit=False)
            user.customer_details = cust
            user.save()

    else:
        customer_form=CustomerRegister()
        login_form = LoginRegister()
    return render(request,'register2.html',{'customer_form':customer_form,'login_form':login_form})




