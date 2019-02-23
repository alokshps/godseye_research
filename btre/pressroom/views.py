from django.shortcuts import render
from django.utils import timezone
from .models import Room


def press_room(request):
    rooms = Room.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    rooms = Room.objects.filter(is_published=True)

    return render(request, 'pressroom/press_room.html', {'rooms': rooms})
