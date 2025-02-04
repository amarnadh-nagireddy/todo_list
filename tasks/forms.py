from django import forms
from .models import Task
from datetime import date 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'last_date', 'priority']
        widgets = {
            'last_date': forms.DateInput(attrs={
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d')
                }),
        }
