from django.db import models as m
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Category(m.Model):
    name = m.CharField(max_length=100)
    description = m.CharField(max_length=300, blank=True)
    slug = m.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
        
   

def set_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(set_slug, sender=Category)