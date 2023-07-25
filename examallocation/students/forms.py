from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from students.accountStatus import ACCOUNT_STATUS
from students.models import Profile
from .gender import GENDER
from .departments import DEPARTMENTS    
from .levels import LEVEL


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


YEARS = [x for x in range(1960,2021)]

class ProfileForm(forms.ModelForm):
    phoneNumber = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    regno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    dept = forms.ChoiceField(choices=DEPARTMENTS, widget=forms.Select(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'class':'form-control'}))
    level = forms.ChoiceField(choices=LEVEL, widget=forms.Select(attrs={'class':'form-control'}))
    dob = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))


    class Meta:
        model = Profile
        fields = ('phoneNumber', 'regno', 'dept', 'gender', 'level', 'dob',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['gender'].label = "Gender:"
        self.fields['phoneNumber'].label = "Phone Number:"
        self.fields['regno'].label = "Reg Number:"
        self.fields['level'].label = "Level:"
        self.fields['dept'].label = "Department:"
        self.fields['dob'].label = "Date Of Birth:"