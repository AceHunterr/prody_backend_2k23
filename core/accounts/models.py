from django.contrib.auth.models import AbstractUser
from django.db import models
import random


def generate_default_user_id():
    return f'#PY{random.randint(100000000, 999999999)}'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_id = models.CharField(
        max_length=12, unique=True, default=generate_default_user_id)

    def __str__(self):
        return f'{self.username} - {self.user_id}'
