from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class CustomAuthForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower().strip()
        if not email:
            raise ValidationError("Email field cannot be empty.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            msg = "Invalid email or password."
            logger.error(f"Authentication failed for email: {email}. Error: {msg}")
            raise ValidationError(msg)

        return cleaned_data

class LearnerRegistrationForm(UserCreationForm):
    admission_number = forms.CharField(required=True, help_text="Please enter your admission number.")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'admission_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(LearnerRegistrationForm, self).save(commit=False)
        user.is_learner = True
        user.username = self.cleaned_data.get('admission_number')  # Use the provided admission number as the username
        if commit:
            try:
                user.save()
                logger.info(f"Learner {user.email} registered successfully with admission number {user.username}.")
            except Exception as e:
                logger.error(f"Failed to register learner {user.email}. Error: {e}", exc_info=True)
                raise e
        return user