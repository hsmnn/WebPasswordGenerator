from django.db import models

class Password(models.Model):
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.password