from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy 
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('blog')

    def get_object(self):
        return self.request.user

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('show_profile', args=[str(self.kwargs['pk'])])

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('show_profile', args=[str(self.kwargs['pk'])])
