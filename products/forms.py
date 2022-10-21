from .models import PositiveReview
from django import forms
from django.forms import TextInput


class PositiveReviewForm(forms.ModelForm):
    class Meta:
        model = PositiveReview
        fields = ('body', 'name',)
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'readonly': '',})
        }
