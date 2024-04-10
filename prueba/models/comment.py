from django.db import models
from .feacture import Feature

class Comment(models.Model):
    feature = models.ForeignKey(Feature, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()

    def _str_(self):
        return f"{self.id} - {self.title}"