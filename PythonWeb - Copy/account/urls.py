from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('<int:pk>/edit/', views.UserEditView.as_view(), name="edit_account"),
    path('password/', views.ChangePasswordView.as_view(),name="change_password"),

]
