from django.urls import path

from GARAGE_APP import views

urlpatterns = [
     path("index",views.index,name="index"),
     path("admin",views.admin,name="admin"),
     path("service_center",views.service_center,name="service_center"),
     path("customer",views.customer,name="customer"),
     path("login_view",views.login_view,name="login_view"),


]