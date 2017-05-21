from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from loginsys import views


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class MyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )
        if user.username.startswith('b'):
            raise forms.ValidationError(
                "Sorry, accounts starting with 'b' aren't welcome here.",
                code='no_b_users',
            )


class Edituserform(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
