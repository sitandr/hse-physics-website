from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class EmailUserManager(BaseUserManager):
    
    def create_user(self, email, password, role = ''):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        
        from .profiles import roles # not the best solution, but possible;
        # we need to import it here to avoid cross-reference
        # (to create roles we need role classes, they need user to be created,
        # and user needs this class

        if not role in roles:
            raise ValueError('Invalid role: ' + str(role))

        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        roles[role].objects.create(user=user)

        
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
    username = models.CharField(max_length=30, default = 'user')
    email = models.EmailField('email address', unique=True) # changes email to unique and blank to false
    
    objects = EmailUserManager()
    REQUIRED_FIELDS = []
    role = models.CharField(max_length=30) # just a holder for generating profile

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


