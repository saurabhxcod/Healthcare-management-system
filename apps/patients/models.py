from django.db import models
from django.conf import settings

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    disease = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
