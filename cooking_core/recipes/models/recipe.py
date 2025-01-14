from django.db import models

from cooking_core.general.models import CreatedModified


class Recipe(CreatedModified):
    creator = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    balance = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    image_url = models.URLField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
