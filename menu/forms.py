from django import forms
from .models import Judgment

class JudgmentForm(forms.ModelForm):
    class Meta:
        model = Judgment
        fields = ['title', 'date', 'court', 'text']