from django.db import models


class Snippet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=50)

    class Meta:
        ordering = ('-created_at', )


