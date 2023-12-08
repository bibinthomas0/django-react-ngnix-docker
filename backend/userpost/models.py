from django.db import models

class Posts(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField()
    is_active = models.BooleanField(default=True)

