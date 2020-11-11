from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class ProfileManager(models.Manager):
    def search(self,query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
                Q(user__username__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)

    objects = ProfileManager()

    