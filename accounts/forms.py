from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Username')}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(_("Invalid Username"))
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError(_("Invalid Password"))
        elif user is None:
            pass
        else:
            return password

class RegistrationForm(forms.ModelForm):
    new_username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Username'), 'class': 'form-control'}))
    new_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Password'), 'class': 'form-control'}))
    password_conf = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Confirm password'), 'class': 'form-control'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('First Name'), 'class': 'form-control'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Last Name'), 'class': 'form-control'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': _('Email'), 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_new_username(self):
        new_username = self.cleaned_data.get("new_username")
        user_count = User.objects.filter(username=new_username).count()
        if user_count > 0 :
            raise forms.ValidationError(_("This username has already been registered"))
        return new_username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        if user_count > 0 :
            raise forms.ValidationError(_("This email has already been registered"))
        return email

    def clean_password_conf(self):
        password = self.cleaned_data.get('new_password')
        password_conf = self.cleaned_data.get('password_conf')
        if password and password_conf and password != password_conf:
            raise forms.ValidationError(_("Passwords do not match"))
        return password