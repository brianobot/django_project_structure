import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-date_created"]

    def __str__(self):
        return f"< {type(self).__name__}({self.id}) >"
