from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=100, blank=True, default="", primary_key=True
    )
    author = models.CharField(max_length=100, blank=True, default="")
    date = models.DateTimeField()

    class Meta:
        ordering = ["author"]
