from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django import forms
class signUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        widgets={
            'email': forms.EmailInput(attrs={
                'required':True,
                'placeholder':'Enter Email',
                'autofocus':True
            }),
            'username': forms.TextInput(attrs={
                'required':True,
                'placeholder':'Enter User name',
                'autofocus':True
            }),
        }

    def __init__(self, *args, **kwargs):
        super(signUpForm,self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder':'Enter Password'}
        self.fields['password2'].widget.attrs = {'placeholder':'Enter Confirm Password'}


# in login form it provide only username and password field
class LoginForm(AuthenticationForm):
    class Meta:
        fields='__all__'
        