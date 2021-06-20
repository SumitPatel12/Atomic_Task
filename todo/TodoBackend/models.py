from django.db import models
import uuid
from User.models import User


class Todo(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)
    completed = models.BooleanField(default = False)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    todo_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title