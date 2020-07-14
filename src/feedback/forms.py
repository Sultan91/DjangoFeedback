from django import forms
from .models import Feedback


class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'title',
            'start_date',
            'end_date',
            'description',
        ]

