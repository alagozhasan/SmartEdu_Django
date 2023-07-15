from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import ContactModel
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
        
    ))
class RegisterForm(UserCreationForm):
      first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name'
    }))
      last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Last Name'
    }))
      username = forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Username'
        }))
      email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))  
      password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password' 
    }))
      password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password Confirm'
    }))  
      class Meta:
          model=User
          fields=[
              'first_name','last_name',
              'username','email',
              'password1','password2'
          ]
      
      
      
      
      
      
# class ContactForm(forms.ModelForm):
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "First Name",
#             }
#         )
#     )
#     #  <input type="text" name="first_name" id="first_name" class="form-control" placeholder="First Name">
#     last_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={"class": "form-control", "placeholder": "Last Name"}
#         )
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
#     )
#     phone = forms.CharField(
#         widget=forms.TextInput(
#             attrs={"class": "form-control",
#                    "placeholder": "Phone Number"}
#         )
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "lorem ipsum dolor sit amet... ... ",
#             }
#         )
#     )

#     class Meta:
#         model = ContactModel
#         fields = ["first_name", "last_name", "email", "phone", "message"]
