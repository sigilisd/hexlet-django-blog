from django import forms
from django.forms import ModelForm
from .models import Article, ArticleComment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]

class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data