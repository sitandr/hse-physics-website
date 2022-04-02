from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from . import Profile

class EmailUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.profile = Profile.objects.create()
        user.save(using=self._db)

        
        
        return user

    def create_superuser(self, email, password, role = ''):

        user = self.create_user(
            email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class EmailUser(AbstractUser):
    
    USERNAME_FIELD = 'email'

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, default='user')
    email = models.EmailField('email address', unique=True) # changes email to unique and blank to false
    
    objects = EmailUserManager()
    REQUIRED_FIELDS = []

    # copy-paste from https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager

    def __str__(self):
        return str(self.profile) if hasattr(self, 'profile') else 'noprofile' 

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


@receiver(post_delete, sender=EmailUser)
def auto_delete_user(sender, instance, **kwargs):
    instance.profile.delete()
