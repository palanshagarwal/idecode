from django.db import models


class Snippet(models.Model):
    code_id = models.AutoField(primary_key=True)
    text = models.TextField()
    download_url = models.URLField(max_length=100, blank=True)
    file_name = models.CharField(max_length=50, blank=True)
    lang = models.CharField(max_length=50, blank=True)
    run_count = models.IntegerField(default=0)
    write_key = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.code_id)
