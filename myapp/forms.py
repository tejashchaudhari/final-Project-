from django import forms
from .models import userSignup,feedback,milanagent,blogreply

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'


class UpdateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','city','state','mobile']


class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'

class milanagentForm(forms.ModelForm):
    class Meta:
        model=milanagent
        fields='__all__'

class blogreplyForm(forms.ModelForm):
    class Meta:
        model=blogreply
        fields='__all__'