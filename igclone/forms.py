from cProfile import label
import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Textarea
from .models import Image,Comments, Profile
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=50)
    email = forms.EmailField(label='Email')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password1']
        help_texts = {'username':None, 'password2':None}

User._meta.get_field('email')._unique=True

