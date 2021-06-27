from django.db import models


class CustomBotDataset(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
