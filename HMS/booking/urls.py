from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking_list, name='booking-list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking-detail'),
]
