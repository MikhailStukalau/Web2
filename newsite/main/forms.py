from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
        }