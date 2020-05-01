from django import forms
from .models import ReadingEvent

class CreateEvent(forms.ModelForm):
    class Meta:
        model = ReadingEvent
        fields = ('title', 'text')