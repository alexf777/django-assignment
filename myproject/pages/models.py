from django.db import models

class Page(models.Model):
    header = models.CharField(max_length=255)
    body = models.TextField()
    footer = models.CharField(max_length=255)

def __str__(self):  
    return self.header