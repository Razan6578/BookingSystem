from django.shortcuts import render
from .models import Room, Booking

# Create your views here.

# Функція представлення списку всіх кімнат
def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request=request, template_name="rooms/room_list.html", context=context)