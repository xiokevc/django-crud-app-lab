from django import forms
from .models import Task, Subtask


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_complete']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description (optional)',
                'rows': 4
            }),
            'is_complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Details',
            'is_complete': 'Completed?',
        }


class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['title', 'is_done']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtask title'
            }),
            'is_done': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Subtask Title',
            'is_done': 'Done?',
        }
