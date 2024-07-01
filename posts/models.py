from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    modifiedAt = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title