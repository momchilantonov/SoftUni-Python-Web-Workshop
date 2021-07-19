from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, ):
        if not email:
            raise ValueError('You must provide an email.')

        if not username:
            raise ValueError('You must provide username.')

        if not first_name:
            raise ValueError('You must provide first name.')

        if not last_name:
            raise ValueError('You must provide last name.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user



class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=60,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'


