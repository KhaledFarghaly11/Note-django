from django import forms
from django.contrib.auth.models import User
from account.models import AmountUser , Debose , Debit

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class Amount_user(forms.ModelForm):
    class Meta:
        model = AmountUser
        fields = ('amount',)



class Debose_form(forms.ModelForm):
    class Meta:
        model = Debose
        fields = ('debose',)


class Debit_form(forms.ModelForm):
    class Meta:
        model = Debit
        fields = ('debit',)      




