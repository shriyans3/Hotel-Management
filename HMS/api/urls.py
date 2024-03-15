from django.urls import path
from . import views
import room.views
import booking.views

urlpatterns = [
    # Room URLs
    path('rooms/', room.views.room_list, name='room-list'),
    path('rooms/<int:room_id>/', room.views.room_detail, name='room-detail'),

    # Booking URLs
    path('bookings/', booking.views.booking_list, name='booking-list'),
    path('bookings/<int:booking_id>/', booking.views.booking_detail, name='booking-detail'),
]
