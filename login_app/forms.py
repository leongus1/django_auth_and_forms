from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            'username': _('Email Address'),
        }
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        # user.username = self.cleaned_data['']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user




class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)




# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name', 'last_name', 'username', 'password']
#         labels ={
#             'username': _('Email Address'),
#         }
#         help_texts = {
#             'username': _('')
#         }
        
        
