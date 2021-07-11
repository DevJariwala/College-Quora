from django import forms
from django.forms import fields, widgets
from .models import Question, Response


# using this form we can use our own model which we have created
class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','body']
        widgets={
            'title': forms.TextInput(attrs={
                'autofocus':True,
                'placeholder':'Start your question with "What", "How", "Why", etc.'
            }),
            'body': forms.TextInput(attrs={
                'autofocus':True,
                'required':False,
            })
        }

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets={
            'body': forms.Textarea(attrs={
                'cols':50,
                'rows':5,
                'placeholder':"Enter your answer"
            })
        }




# class signUpForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['username','email','password1','password2']
#         widgets={
#             'email': forms.EmailInput(attrs={
#                 'required':True,
#                 'placeholder':'Enter Email',
#                 'autofocus':True
#             }),
#             'username': forms.TextInput(attrs={
#                 'required':True,
#                 'placeholder':'Enter User name',
#                 'autofocus':True
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super(signUpForm,self).__init__(*args, **kwargs)
#         self.fields['password1'].widget.attrs = {'placeholder':'Enter Password'}
#         self.fields['password2'].widget.attrs = {'placeholder':'Enter Confirm Password'}