from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserInfo


def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError(
            'Name and job title should not contain numbers.')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['job_title']

    job_title = forms.CharField(
        max_length=255,
        validators=[validate_no_numbers],
        widget=forms.TextInput(attrs={'placeholder': 'Your job title'}),
        error_messages={
            'min_length': 'Job title should be at least 14 characters long.'}
    )

class SignupForm(UserCreationForm):
    jobtitle = forms.CharField(max_length=255, required=True,
                                help_text='Required. Should be at least 14 characters long.',
                                validators=[validate_no_numbers],
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Your job title'}),
                                error_messages={
                                    'min_length': 'Job title should be at least 14 characters long.'
                                })

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'jobtitle')


        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Your username',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email address',
                'class': 'form-control'
                }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Enter your password',
                'class': 'form-control'
                }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat your password',
                'class': 'form-control'
                }),
            'jobtitle': forms.TextInput(attrs={
                'placeholder': 'Enter your job title',
                'class': 'form-control'
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))
