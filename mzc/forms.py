from django import forms
from .models import faculty
class FacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields='__all__'