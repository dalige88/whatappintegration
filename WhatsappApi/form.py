from typing import Dict
from django.db.models import fields
from .models import *
from django import forms
from django.forms import ModelForm, widgets,DateInput,FileInput,TextInput
from typing import Dict

class RegisterForm(ModelForm):
    class Meta:
        model = RegisterPage
        fields = '__all__'
      