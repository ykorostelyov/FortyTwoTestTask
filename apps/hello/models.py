from django.db import models


# mycard model
class Mycard(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    jabber = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    bio = models.TextField()
    other_contacts = models.TextField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
