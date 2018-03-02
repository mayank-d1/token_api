from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name


class Token(models.Model):
    user_id = models.CharField(max_length=10, unique=True, null=False)
    token = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4())
    expiry_date = models.DateTimeField(default=(timezone.now() + timedelta(days=2)))

    def __str__(self):
        return self.user_id


