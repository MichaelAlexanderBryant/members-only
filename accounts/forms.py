from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)

class MemberCodeForm(forms.Form):
    membership_code = forms.CharField(max_length=250)