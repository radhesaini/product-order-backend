from datetime import datetime
from django.db import models

class Base(models.Model):
    is_deleted = models.BooleanField(default=False)
    modified_date = models.DateTimeField(auto_now_add=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)