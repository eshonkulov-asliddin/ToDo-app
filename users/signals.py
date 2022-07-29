from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User


def CreateProfile(sender, created, instance, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
        )

post_save.connect(CreateProfile, sender=User)