from django import forms
from .models import SignUp

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('__all__')
