from django.db import models as m

# Create your models here.
class Category(m.Model):
    name = m.CharField(max_length=100)
    description = m.CharField(max_length=300)
    slug = m.SlugField(unique=True)

    def __str__(self):
        return self.name
        
   