from django import forms
from . models import user,resetpassword
class signupform(forms.Form):
    name=forms.CharField(widget=forms.TextInput())
    loginid=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
    emailaddress = forms.CharField(widget=forms.TextInput())
    phonenumber = forms.IntegerField(widget=forms.NumberInput())

class resetform(forms.Form):
    yourloginid = forms.CharField(widget=forms.TextInput())
    enterpassword = forms.CharField(widget=forms.PasswordInput())
    confirmpassword = forms.CharField(widget=forms.PasswordInput())