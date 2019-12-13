from django import forms
from .models import Feedback


class Feedbackform(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"autofocus": ""}))

    class Meta:
        model = Feedback
        fields = ['text','name','contact']
