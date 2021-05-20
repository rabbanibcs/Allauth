from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from tlou.models import userdtl


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class UserdtlUpdateForm(ModelForm):
    class Meta:
        model = userdtl
        fields = ('city','psn','xbl','zipcode')
