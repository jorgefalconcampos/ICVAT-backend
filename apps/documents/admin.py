from django.contrib import admin
from . models import Document
from django_summernote.admin import SummernoteModelAdmin

class DocumentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

admin.site.register(Document, DocumentAdmin)