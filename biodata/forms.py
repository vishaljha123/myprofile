from django import forms
from .models import Userinfo




class Userinformation(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ('first_name', 'last_name', 'email_add','phone','position','education','work_exp','resume','video_resume',)