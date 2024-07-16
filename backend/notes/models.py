from django.db import models

class Note(models.Model):
    header = models.CharField("Header", max_length=128)
    body = models.CharField("Body", max_length=1024)
    image = models.ImageField("Image", null=True)
    created_date = models.DateField("Created Date", auto_now_add=True)

    def __str__(self):
        return (self.header + '\n' + self.body[0:30])