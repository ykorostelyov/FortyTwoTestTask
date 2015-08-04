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


#insert
#mycard = Mycard.objects.create(
#    fName="Yuriy",
#    lName="Korostelyov",
#    bDate="1983-01-13",
#    eMail="ykorostelyov@gmail.com",
#    Jabber="ykorostelyov@khavr.com",
#    Skype="yuriy.torhammer",
#    bio="Was born in Kiev. Studied in school #210, then in Kiev Polytechnical Institute. Worked in some banks.",
#    otherContacts="mob: 067.693.61.96"
#)


#commit
#mycard.save()