import uuid
from django.db import models as m
from categories.models import Category
from users.models import User
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save, post_save

class Document(m.Model):
    document_id = m.CharField(max_length=100, null=False, blank=False, unique=True)
    author = m.ForeignKey(User, on_delete=m.CASCADE, related_name="author", null=False, blank=False)
    title = m.CharField(max_length=200, null=False, blank=False)
    slug = m.SlugField(unique=False, null=True, blank=False)
    category = m.ForeignKey(Category, on_delete=m.CASCADE, null=False, blank=False)
    body = m.TextField()
    tags = TaggableManager()
    created_date = m.DateField(auto_now_add=True, null=False, blank=False)
    modified_date = m.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.document_id} | {self.title}"



def set_document_id(sender, instance, *args, **kwargs):
    if not instance.document_id:
        instance.document_id = str(uuid.uuid4())[:18]



pre_save.connect(set_document_id, sender=Document)