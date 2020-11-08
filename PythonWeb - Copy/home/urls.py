from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('profile/<int:pk>/', views.ShowProfileView.as_view(), name="show_profile"),
    #path('profile/<int:pk>/edit/', views.EditProfileView.as_view(), name="edit_profile"),
    path('profile/<int:pk>/edit/', views.profile_update, name="edit_profile"),
    path('profile/<int:pk>/create/', views.CreateProfileView.as_view(), name="create_profile"),
    
]
