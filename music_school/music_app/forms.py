"""
The form to be displayed on the page, specifying the input types.
"""

from django import forms
from music_app.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


SKILLS_CHOICES = [('Beginner','Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')]
GENDER_CHOICES = [('M', 'Male'),('F', 'Female')]

#Form used in the registration page
class SignUpForm(forms.ModelForm):
    #specify variables and the input type
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    age = forms.IntegerField(max_value=120, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=250, required=True)
    skill_level = forms.ChoiceField(choices=SKILLS_CHOICES)

    class Meta:
        model = UserProfile

        #specify the fields to fill out
        fields = (
            'first_name',
            'last_name',
            'gender',
            'age',
            'email',
            'address',
            'skill_level',
            )