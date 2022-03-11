from django.db import models as m


class Tag(m.Model):
    created_date = m.DateField(auto_now_add=True, null=False, blank=False)

    class Meta:
        app_label = 'tags'

    def __str__(self):
        return self.created_date
