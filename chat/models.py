from django.db import models
from users.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message {self.pk}'

    class Meta:
        ordering = ['-timestamp']