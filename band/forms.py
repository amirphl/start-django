from django import forms
from django.contrib.auth.models import User


# class BandContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    # def clean_message(self):
    #     username = self.cleaned_data.get("username")
    #     dbuser = User.objects.filter(name=username)
    #
    #     if not dbuser:
    #         raise forms.ValidationError("User does not exist in our db!")
    #     return username

    def clean_username(self):
        username = self.cleaned_data.get("username")
        dbuser = User.objects.filter(username=username)

        if not dbuser:
            print("User does not exist in our db!")
            raise forms.ValidationError("User does not exist in our db!")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        dbuser = User.objects.filter(username=username, password=password)

        if not dbuser:
            print("incorrect pass!!")
            raise forms.ValidationError("incorrect pass!!")
        return password


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            dbuser = User.objects.get(username=username)
            if dbuser:
                print("Username exists in our db!")
                raise forms.ValidationError("Username exists in our db!")
        except User.DoesNotExist:
            pass
        return username
