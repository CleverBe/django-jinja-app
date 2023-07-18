from django import forms
from .models import Task


class newTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type a description'}),
            'project': forms.Select(attrs={'class': 'form-control'})
        }


class newProjectForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type a name'}))
