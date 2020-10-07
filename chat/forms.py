from django import forms
from .models import Rooms , Participants

class GroupForm(forms.ModelForm):
    class Meta:
        model= Rooms
        fields='__all__'