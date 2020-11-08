from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from home.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','user')

        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'user': forms.TextInput(attrs={'class':'form-control', 'id':'user', 'value':'','type':'hidden'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =('username', 'password1','password2','first_name','last_name','email')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')
    

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1','new_password2')


