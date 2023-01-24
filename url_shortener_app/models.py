import uuid
from django.db import models

class UrlModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    main_url = models.CharField(max_length=255)
    shrtened_ur = models.CharField(max_length=255, unique=True)
    total_views = models.IntegerField(default=0, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    edit_password = models.IntegerField()

    class Meta:
        db_table = "urls"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title
