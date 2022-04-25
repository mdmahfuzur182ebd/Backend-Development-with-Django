from django import forms
from django.core import validators



class user_name(forms.Form):
    first_name = forms.CharField(label='Your First Name', required=False, initial="Type your Name")
    last_name = forms.CharField(label='Your Last Name',required=False,  widget = forms.TextInput(attrs={'placeholder':"Type Your Last Name"}))
    dob = forms.DateField(label="Date of Birth", required=False,widget=forms.TextInput(attrs={'type':'date'}))
    Email = forms.EmailField(required=False, widget = forms.TextInput(attrs={'placeholder':"Type Your valid Email"}))
