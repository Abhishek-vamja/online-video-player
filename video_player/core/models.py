"""
Core model for apps.
"""
from django.db import models

import uuid

class BaseModel(models.Model):
    """Base Model."""
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)