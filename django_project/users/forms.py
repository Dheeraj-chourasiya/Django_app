
from django import forms 
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from users.models import Profile

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField() # this function takes  an argument which is default is  required = true 

    class Meta:
        model = User # we are speifying a model that we want this form  to intract with whenever this form validate it creates a new user 
        fields = ['username', 'email', 'password1','password2']
        # this class meta gives us a nested namespace for configuration 
        # and keeps the configurations in one place and within the 
        # configurations we  are saying the model that will be affected is the user model
        #so for exampe when we do a form.save() its going to affect the user model 
class UserUpdateForm(forms.ModelForm):
        email= forms.EmailField()
        class Meta:
             model = User  
             fields = ['username', 'email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['image']             


        