
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewEventForm, EditEventForm
from .models import Category, Event
from django.db.models import Q
def events(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    events = Event.objects.filter(is_liked=True)

    if category_id:
        events = events.filter(category_id=category_id)

    if query:
        events = events.filter(Q(event_name__icontains=query) | Q(description__icontains=query))

    return render(request, 'core/events.html', {
        'events': events,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    related_events = Event.objects.filter(category=event.category, is_liked=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'event': event,
        'related_event': related_events
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
    else:
        form = NewEventForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New event',
    })

@login_required
def edit(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)

    if request.method == 'POST':
        form = EditEventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=event.id)
    else:
        form = EditEventForm(instance=event)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit event',
    })

@login_required
def delete(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    event.delete()
    return redirect('dashboard:index')



