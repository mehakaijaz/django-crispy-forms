from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class UniversityForm(forms.ModelForm):
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_action = reverse_lazy('index')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','Submit'))
    
    SUBJECT_CHOICES=(
        (1,'web d'),
        (2,'comp. science'),
        (3,'data science'),
    )
    
    #name=forms.CharField()
    
    age=forms.IntegerField()
    subject=forms.ChoiceField(choices=User.Subjects.choices)
                              
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()}))
    
    class Meta:
        model=User
        fields=('username','password','date_of_birth','subject')
        widgets={
            'password':forms.PasswordInput()
        }
        
    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user