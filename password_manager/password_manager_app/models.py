# models.py

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser  # AbstractUser sınıfını içe akt
from django.utils.translation import gettext_lazy as _  # gettext_lazy sınıfını içe aktarın
from django.contrib.auth.models import Group, Permission  # Group ve Permission sınıflarını içe aktarın


# models.py

from django.db import models
from django.contrib.auth.models import User

class Password(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_passwords"  # Örnek bir related_name ekleyin
    )
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.website



class CustomUser(AbstractUser):
    # İhtiyaca göre ek alanlar ekleyebilirsiniz
    pass

    class Meta:
        permissions = [
            ("can_change_password", "Can change password"),
        ]

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_users"  # Örnek bir related_name ekleyin
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_users_permissions"  # Örnek bir related_name ekleyin
    )
