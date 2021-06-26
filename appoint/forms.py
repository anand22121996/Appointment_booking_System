from django import forms
from . models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
	input_type = 'date'

class Appointment_Form(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['id','adate','afrom_time','ato_time']
		widgets = {'adate':forms.DateInput(attrs={'type':'date'}),'afrom_time':forms.TimeInput(attrs={'type':'time'}),'ato_time':forms.TimeInput(attrs={'type':'time'})}






class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']