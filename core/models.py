from django.db import models

# Create your models here. (database stuff)

#Creates a table in the database called "List" with 2 Columns
class List(models.Model):
    #Columns defined here
    item  = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
