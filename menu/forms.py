from django import forms
from models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'parent', 'label', 'url', 'named_url']