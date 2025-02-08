from django.db import models

class Message(models.Model):
    content = models.TextField()
    is_spam = models.BooleanField(default=False)

