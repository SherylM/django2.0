from django.db import models

# Create your models here.

class Textbook(models.Model):
    textbooktitle = models.CharField(max_length=250)
    textbookauthor = models.CharField(max_length=250)
    textbookpublisher = models.CharField(max_length=250)
    textbooklocation = models.CharField(max_length=400)
    textbookimage = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.textbooktitle + ' - ' + self.textbookauthor

class Prepbook(models.Model):
    prepbooktitle = models.CharField(max_length=250)
    prepbookauthor = models.CharField(max_length=250)
    prepbookpublisher = models.CharField(max_length=250)
    prepbooklocation = models.CharField(max_length=400)
    prepbookimage = models.CharField(max_length=1000)

    def __str__(self):
        return self.prepbooktitle + ' - ' + self.prepbookauthor
    
