from django.db import models

from django.db import models

class Car(models.Model):
    ismi = models.CharField(max_length=255)
    rangi = models.TextField()
    turi = models.DateTimeField(auto_now_add=True)
    rasmi = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.ismi

