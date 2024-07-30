from django.db import models

class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    header = models.TextField("Header", blank=True, max_length=128)
    body = models.TextField("Body", blank=True)
    image = models.ImageField("Image", blank=True, upload_to=f'files/{id}' )
    created_date = models.DateTimeField("Created Date", auto_now_add=True)
    last_modified = models.DateTimeField('Last Modified Date', auto_now=True)

    def __str__(self):
        return (self.header + '\n' + self.body[0:30])