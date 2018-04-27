from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


SKILLS_CHOICES = ((1, ('Beginner')), (2, ('Intermediate')), (3, ('Expert')))
GENDER_CHOICES = ((1, ('Male')), (2, ('Female')))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=250, required=True)
    age = forms.IntegerField(max_value=120, required=True)
    skill_level = forms.ChoiceField(choices=SKILLS_CHOICES,required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES,required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'gender',
            'age',
            'email',
            'address',
            'skill_level',
            'username',
            'password1',
            'password2'
        ]
        #Add role? e.g. student or teacher

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=250, required=True)
    age = forms.IntegerField(max_value=120, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES,required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'email',
            'address',
            'age',
            'gender',
            'password',
        )