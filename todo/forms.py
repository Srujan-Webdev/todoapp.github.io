from django import forms
from .models import Task

#Adding below date picker for sending reminders mail to complete the task
class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    content = forms.CharField(label='Task to be added', widget=forms.TextInput(
        attrs={'placeholder': 'Add Task here...'}))

    class Meta:
        model = Task
        #Adding below date picker for sending reminders mail to complete the task
        fields = ['content', 'time_tobe_completed']
        #Adding below date picker for sending reminders mail to complete the task
        widgets = {
            'time_tobe_completed': DateInput()
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = '__all__'
        fields = ['content', 'completed', 'time_tobe_completed']
        widgets = {
            'time_tobe_completed': DateInput()
        }
