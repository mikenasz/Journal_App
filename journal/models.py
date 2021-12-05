from django.db import models

# Create your models here.
class journal(models.Model):
    title = models.CharField(max_length=200)
    entry = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']