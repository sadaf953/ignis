from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Event

@login_required
def index(request):
    events = Event.objects.filter(user=request.user)

    return render(request, 'dashboard/index.html', {
        'events': events,
    })

def detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    related_events = Event.objects.filter(category=event.category, is_liked=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'event': event,
        'related_event': related_events
    })

