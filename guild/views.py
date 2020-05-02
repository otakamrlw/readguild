from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import ReadingEvent



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def event_list(request):
    events = ReadingEvent.objects.filter(created_date=timezone.now()).order_by('created_date')
    return render(request, 'guild/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(ReadingEvent, pk=pk)
    return render(request, 'guild/event_detail.html', {'event': event})