import datetime

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    deadline = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["completed"]

    def __str__(self) -> str:
        return self.content
