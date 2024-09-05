from django import forms

# Form for submiting the new task that user will enter
class TaskForm(forms.Form):
    task = forms.CharField(max_length=64, label="Task Heading")
    description = forms.CharField(min_length=16, max_length=264, label="Task Description")

