from django import forms
from django.conf import settings
from project.models import User, Reservation, Menu


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last name'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email Adress'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'picture', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'picture', 'bio',
                  'phone_number', 'email', 'website']


class ReservationForm(forms.ModelForm):
    time = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'timepicker',
                                      'class': 'input-group'}))
    date_reserved = forms.DateField(widget=forms.DateInput(
        attrs={'id': 'datepicker'}), required=True)

    class Meta:
        model = Reservation
        fields = ['first_name',
                  'email', 'people', 'time',
                  'phone', 'date_reserved', 'status','location','comment']


class AddMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price','picture',
                  'description', 'type', 'category','location']



