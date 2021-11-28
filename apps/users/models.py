from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activated_account = models.BooleanField(default=False)
    bio = models.TextField(blank=True)