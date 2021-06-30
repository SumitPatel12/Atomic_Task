from django.db import models
from django.db import models
from datetime import datetime, date
import uuid


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, unique=True, default=None)
    recovery_email = models.EmailField(max_length=254, blank=True, unique=True, default=None)
    password = models.CharField(max_length=32)
    joining_date = models.DateField(auto_now_add=True, auto_now=False, null=True, blank=True)

    def __str__(self):
        return str(self.user_id)