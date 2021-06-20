from django.db import models
from uuid import uuid4


def generateUUID():
    return (str(uuid4()))


class Todo(models.Model):
    title_id = models.UUIDField(
        primary_key=True,
        default=generateUUID,
        editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    status = models.TextField(default=False)

    def __str__(self):
        return self.title
