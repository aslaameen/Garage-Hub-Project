from django.urls import path

from GARAGE_APP import views, servicecenterviews, customerviews, adminviews
from GARAGE_APP.customerviews import booking_view

urlpatterns = [
     path("",views.index,name="index"),
     path("admin_home",views.admin_home,name="admin_home"),
     path("service_center",views.service_center,name="service_center"),
     path("customer",views.customer,name="customer"),
     path("login_view",views.login_view,name="login_view"),
     path("service_add",views.service_add,name="service_add"),
     path("dash",views.dash,name="dash"),
     path("customer_add",views.customer_add,name="customer_add"),
     path("service_profile",servicecenterviews.service_profile,name="service_profile"),
     path("profile_edit", servicecenterviews.profile_edit, name="profile_edit"),
     path("service_list",servicecenterviews.service_list,name="service_list"),
     path("service_lists",adminviews.service_lists,name="service_lists"),
     path("service_update/<int:id>/", servicecenterviews.service_update, name="service_update"),
     path("service_delete/<int:id>/", servicecenterviews.service_delete, name="service_delete"),
     path("delete_data/<int:id>/", servicecenterviews.service_delete, name="service_delete"),
     path("customer_profile",customerviews.customer_profile,name="customer_profile"),
     path("customer_list",customerviews.customer_list,name="customer_list"),
     path("customer_update/<int:id>/", customerviews.customer_update, name="customer_update"),
     path("customer_delete/<int:id>/", customerviews.customer_delete, name="customer_delete"),
     path("customer_edit",customerviews.customer_edit,name="customer_edit"),
     path("delete_data/<int:id>/",customerviews.customer_delete,name="customer_delete"),
     path('car_add/',customerviews.car_add,name="car_add"),
     path("car_list",servicecenterviews.car_list,name="car_list"),
     path("availability_add",servicecenterviews.availability_add,name="availability_add"),
     path("view_availability",customerviews.view_availability,name="view_availability"),
     path("availability_views",adminviews.availability_views,name="availability_views"),
     path("available_list",servicecenterviews.available_list,name="available_list"),
     path("car_view",customerviews.car_view,name="car_view"),
     path("car_views",adminviews.car_views,name="car_views"),
     path("status_add",servicecenterviews.status_add,name="status_add"),
     path("status_view",servicecenterviews.status_view,name="status_view"),
     path("status_views",customerviews.status_views,name="status_views"),
     path("view_status", adminviews.view_status, name="view_status"),
     path("Log_out",servicecenterviews.Log_out,name="Log_out"),
     path("Log_out",customerviews.Log_out,name="Log_out"),
     path("Log_out",adminviews.Log_out,name="Log_out"),
     path("booking_view",customerviews.booking_view,name="booking_view"),

     path("available_update/<int:id>/", servicecenterviews.available_update, name="available_update"),
     path("available_delete/<int:id>/", servicecenterviews.available_delete, name="available_delete"),
     path("status_update/<int:id>/", servicecenterviews.status_update, name="status_update"),
     path("status_delete/<int:id>/", servicecenterviews.status_delete, name="status_delete"),
     path("customers_list",adminviews.customers_list,name="customers_list"),
     path("car_update/<int:id>/", customerviews.car_update, name="car_update"),
     path("car_delete/<int:id>/", customerviews.car_delete, name="car_delete"),
     path("book_now/<int:id>/",customerviews.book_now,name="book_now"),
     path("booking_view",customerviews.booking_view,name="booking_view"),
     path('booking_status/<int:id>/', servicecenterviews.booking_status, name='booking_status'),
     path("all_bookings",servicecenterviews.all_bookings,name="all_bookings"),
     path("all_bookingss",adminviews.all_bookings,name="all_bookingss"),








]