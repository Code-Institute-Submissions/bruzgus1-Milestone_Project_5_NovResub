from django import forms
from .models import PositiveReview, NegativeReview


class PositiveReviewForm(forms.ModelForm):
    class Meta:
        model = PositiveReview
        fields = ('positive_review', 'name',)


class NegativeReviewForm(forms.ModelForm):
    class Meta:
        model = NegativeReview
        fields = ('negative_review', 'name',)
