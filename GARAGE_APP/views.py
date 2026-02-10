from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render (request,'index.html')




#        base views
# ---------------------------
def admin(request):
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
                return redirect ('admin')
            elif user.is_customer:
                return redirect('service_center')
            elif user.is_servicecenter:
                return redirect('customer')
         else:
             messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')