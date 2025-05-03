from django.db import models

class JobLineage(models.Model):
    job_name = models.CharField(max_length=100)
    upstream = models.JSONField()
    downstream = models.JSONField()

    def __str__(self):
        return self.job_name
