from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validateSymbols

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(validators=[MinLengthValidator(10, 'need at least 10 letters.'), 
                                        validateSymbols])
    createdAt = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    modifiedAt = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title