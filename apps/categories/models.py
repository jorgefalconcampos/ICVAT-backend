from asyncio import constants
from tabnanny import verbose
from tokenize import Triple
from users.models import User
from django.db import models as m
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Category(m.Model):
    name = m.CharField(max_length=30, null=False, blank=False)
    owner = m.ForeignKey(User, on_delete=m.CASCADE, related_name="owner", null=False, blank=False)
    description = m.CharField(max_length=150, null=True, blank=True)
    slug = m.SlugField(unique=False, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
        
   

def set_slug(sender, instance, *args, **kwargs):
    # if not instance.slug:
    instance.slug = slugify(instance.name)

# def verify_name(sender, instance, *args, **kwargs):
#     print(.owner)
#     # lol = Category.objects.filter(owner=self.user)
#     # if instance.name:
#         # print("abr")


pre_save.connect(set_slug, sender=Category)
# pre_save.connect(verify_name, sender=Category)