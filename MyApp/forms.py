from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import TaskCreated
from django import forms


class userCustomForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Conform Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class Created_form(forms.ModelForm):
    task_choices=(
      ('low', 'Low'),
      ('medium', 'Medium'), 
      ('high', 'High'),
      )
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Title'}))
    description =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Descriptions'}))
    due_date=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    priority = forms.ChoiceField(choices=task_choices,widget=forms.Select(attrs={'class':'form-select','type':'select'}))
    created_at=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    updated_at=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    time=forms.CharField(widget=forms.TimeInput(attrs={'class':'form-control','type':'time'}))
    completed = forms.TypedChoiceField(
        label="Completion Status",
        choices=((1, 'Completed'), (0, 'Not Completed')),
        coerce=int,
        widget=forms.RadioSelect,
    )
    
    class Meta:
        model=TaskCreated
        fields = '__all__'
       