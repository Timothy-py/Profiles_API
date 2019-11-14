from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfileManager(BaseUserManager):
    """
    helps django work with the custom user model i.e UserProfile
    """

    def create_user(self, email, name, password=None):
        """
        creates a new user profile object.
        :param email:
        :param name:
        :param password:
        :return:
        """

        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(raw_password=password)
        # user.save(using=self._db)
        user.save()

        return user

    def create_superuser(self, email, name, password):
        """

        :param email:
        :param name:
        :param password:
        :return:
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    This class represents a 'user profile' inside the app
    """

    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        this method gets a user full name
        :return:
        """

        return self.name

    def get_short_name(self):
        """
        this method gets a user's short name
        :return:
        """

        return self.name

    def __str__(self):
        """
        django uses this method to return objects call to string
        :return:
        """

        return self.email


