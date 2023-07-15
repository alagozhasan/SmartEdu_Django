from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }
        )
    )
    #  <input type="text" name="first_name" id="first_name" class="form-control" placeholder="First Name">
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Phone Number"}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "lorem ipsum dolor sit amet... ... ",
            }
        )
    )

    class Meta:
        model = ContactModel
        fields = ["first_name", "last_name", "email", "phone", "message"]
