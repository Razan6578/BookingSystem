from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("rooms/", views.rooms_list, name="rooms"),
    path("booking/", views.book_room, name="booking"),
    path("about/", views.about, name="about"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
]