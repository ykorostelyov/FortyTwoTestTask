from django.db import models

# my model
class Mycard(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    bDate = models.DateField()
    eMail = models.EmailField()
    Jabber = models.CharField(max_length=100)
    Skype = models.CharField(max_length=100)
    bio = models.CharField(max_length=1024)
    otherContacts = models.CharField(max_length=200)

