from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=UserProfile.ROLES)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        role = self.cleaned_data["role"]

        if commit:
            user.userprofile.role = role
            user.userprofile.save()
        return user
