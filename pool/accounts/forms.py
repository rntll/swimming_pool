from django import forms
from .models import UserProfile, Review, Comment, Info
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, TextInput, NumberInput, DateInput


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['user_profile', 'age', 'date_of_birth','phone_number', 'swimming_level']
        widgets = {
            'user_profile': forms.HiddenInput(),

            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "date_of_birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            })}


class AllUsersForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['user_profile', 'age', 'date_of_birth','phone_number', 'swimming_level']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']