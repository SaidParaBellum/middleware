from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()
        return user