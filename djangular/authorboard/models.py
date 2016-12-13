from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Author(models.Model):
    title = models.TextField(max_length=200)
    author = models.TextField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Author:{}".format(self.title)
# Create your models here.
