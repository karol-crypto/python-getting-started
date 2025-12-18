from django.db import models
class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
class Greeting(models.Model):
    message = models.CharField(max_length=255, default="Hello")