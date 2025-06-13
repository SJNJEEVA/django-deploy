from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('profile_pic',)
        
