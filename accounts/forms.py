from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs) -> None:
        super(CreateUserForm, self).__init__(*args, **kwargs)
    
        for field in ['username','email','password1','password2']:
            self.fields[field].help_text = None

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'