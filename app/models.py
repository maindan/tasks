from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200, null=False)
    first_value = models.IntegerField(null=False)
    second_value = models.IntegerField(null=False)
    result = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name