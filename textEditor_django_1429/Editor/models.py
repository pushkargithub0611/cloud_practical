from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class TextModel(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=20)
    content=QuillField()

