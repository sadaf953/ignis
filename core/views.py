from django.shortcuts import render, redirect
from item.models import Category, Event
from .forms import SignupForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def index(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'events': events,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })





@login_required
def like_event(request, event_id):
    if request.method == 'POST' and request.is_ajax():
        try:
            event = Event.objects.get(pk=event_id)
            event.is_liked = not event.is_liked
            event.save()
            return JsonResponse({'status': 'success', 'is_liked': event.is_liked})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Event not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)






@login_required
def toggle_like(request, event_id):
    if request.method == 'POST' and request.is_ajax():
        event = get_object_or_404(Event, pk=event_id)
        if request.user in event.is_liked.all():
            event.is_liked.remove(request.user)
            is_liked = False
        else:
            event.is_liked.add(request.user)
            is_liked = True
        return JsonResponse({'status': 'success', 'is_liked': is_liked})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
