from django.db import models

# Create your models here.

class Task(models.Model):

   text = models.CharField(max_length = 50)
   business = models.CharField(max_length = 250)
   address = models.CharField(max_length = 500)
   taxid = models.CharField(max_length = 50)

   class Meta:
      db_table = "task"