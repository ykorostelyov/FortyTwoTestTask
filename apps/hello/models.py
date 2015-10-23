from django.db import models
from PIL import Image


class Mycard(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    jabber = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    bio = models.TextField()
    other_contacts = models.TextField()
    avatar = models.ImageField(upload_to='avatars',
                               null=True,
                               blank=True)

    def save(self, force_insert=False,
             force_update=False, update_fields=True, using=None):
        super(Mycard, self).save()
        if self.avatar:
            filename = self.avatar.path
            try:
                image = Image.open(filename)
                image.thumbnail((200, 200), Image.ANTIALIAS)
                image.save(filename)

            except IOError as err:
                print err
                self.avatar = None
                super(Mycard, self).save()
        else:
            self.avatar = None
            super(Mycard, self).save()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class RequestInfo(models.Model):
    date = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=1024)
    method = models.CharField(max_length=30)
    path = models.CharField(max_length=1024)
    remote_addr = models.GenericIPAddressField()
    is_viewed = models.BooleanField(default=False)
    is_ajax = models.BooleanField(default=False)
    uri = models.CharField(max_length=1024)
    status_code = models.CharField(max_length=30)
    user_agent = models.CharField(max_length=1024)
    priority = models.IntegerField(max_length=3, default=0)


class EventLog(models.Model):
    date = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=150, default=False)
    event = models.CharField(max_length=20, default=False)

    def __unicode__(self):
        return str(self.date) + ' ' + self.model+' '+self.event
