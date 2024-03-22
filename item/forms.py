from django import forms

from .models import Event

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

from django import forms
from .models import Event

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('category', 'event_name', 'date', 'time', 'location', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'event_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'date': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'time'
            }),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'date', 'time', 'location', 'image', 'is_liked')
        widgets = {
            
            'event_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'date': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'time'
            }),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'is_liked': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-gray-600'
            })
        }
