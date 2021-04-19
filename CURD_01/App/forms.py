from django import forms
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.forms import widgets


# Note Form:---------------
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['headline', 'categories', 'text']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Write Headline Here'}),
            'text': forms.Textarea(attrs={'placeholder': 'Write Text Here'})
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['categories'].empty_label = "Select Category"


# SignUp Form:--------------
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Your Password', 'class': 'myclass'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Your Password Again', 'class': 'myclass'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'myclass', 'placeholder': 'Your Username'}),
            'first_name': widgets.TextInput(attrs={'class': 'myclass', 'placeholder': 'Your First Name'}),
            'last_name': widgets.TextInput(attrs={'class': 'myclass', 'placeholder': 'Your Last Name'}),
            'email': widgets.TextInput(attrs={'class': 'myclass', 'placeholder': 'Your Email'}),
        }
        error_messages = {
            'email': {'required': 'Enter your email address'},
            'first_name': {'required': 'Enter your first name'},
            'last_name': {'required': 'Enter your last name'},
        }


# Login Form:--------------
class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password', 'class': 'myclass'}))

    class Meta:
        model = User
        fields = ['username', 'password']


# Password Change Form:--------------
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Old Password', 'class': 'myclass'}))
    new_password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your New Password', 'class': 'myclass'}))
    new_password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password Again', 'class': 'myclass'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
