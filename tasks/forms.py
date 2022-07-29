
from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']

class DetailTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed'] 
        labels = {
            'completed': 'Complete',
            'name': 'Task title'
        }   

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed']
        labels = {
            'completed': 'Complete',
            'name': 'Task title'
        }  

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description'] 
        labels = {
            'name': 'Title',
            'description': 'Further Note'
        }  
             