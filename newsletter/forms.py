from django import forms
from .models import SignUp, Post


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name", "email"]


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "content"]
