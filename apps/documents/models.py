import uuid
from django.db import models as m
from categories.models import Category
from users.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
from django.db.models.signals import pre_save, post_save

class Document(m.Model):
    document_id = m.CharField(max_length=100, null=False, blank=False, unique=True)
    author = m.ForeignKey(User, on_delete=m.CASCADE, related_name="author")
    title = m.CharField(max_length=200)
    slug = m.SlugField(unique=False)
    category = m.ForeignKey(Category, on_delete=m.CASCADE)
    # body
    tags = TaggableManager()
    created_date = m.DateField(default=timezone.now)

    def __str__(self):
        return self.document_id



def set_document_id(sender, instance, *args, **kwargs):
    if not instance.document_id:
        instance.document_id = str(uuid.uuid4())


pre_save.connect(set_document_id, sender=Document)