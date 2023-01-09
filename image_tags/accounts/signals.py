from rest_framework.authtoken.models import Token
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in, user_logged_out


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
