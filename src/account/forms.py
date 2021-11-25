from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

# Registration form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput())
    class Meta:
        
        model = Account
        fields = ("first_name", "last_name", "email", "password1", "password2")
       
       
# Login form
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Account
        fields = ('email', 'password') 
        
    def clean(self):
        print(self.cleaned_data)
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid email or password') 
