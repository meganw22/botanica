from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Address


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a UserProfile and an associated Address
    when a new User is created.
    """
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        address = Address.objects.create(user=instance)
        user_profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the UserProfile when the User is saved.
    If the UserProfile does not exist, it creates one along with an Address.
    """
    if not hasattr(instance, 'userprofile'):
        user_profile = UserProfile.objects.create(user=instance)
        address = Address.objects.create(user=instance)
        user_profile.save()
    else:
        instance.userprofile.save()
