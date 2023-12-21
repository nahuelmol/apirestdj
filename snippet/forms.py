from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.validators import RegexValidator

from django.forms import ModelForm

from django import forms

class CustomUsernameValidator(RegexValidator):
    regex = r'^[\w.@+-]+$'
    message = 'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'
    flags = 0

class UserCreator(UserCreationForm):

	username = forms.CharField(
        max_length=30,
        validators=[CustomUsernameValidator()],
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
    )
	
	class Meta:
		model = User
		fields = ['username','email','password1','password2']