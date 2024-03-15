from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room-list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room-detail'),
]
