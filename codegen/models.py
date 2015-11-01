from django.db import models


class Snippet(models.Model):
    text = models.TextField()
    lang = models.CharField(max_length=50, blank=True)

