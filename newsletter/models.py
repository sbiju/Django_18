from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(blank=True, null=True, max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated =  models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return self.email


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

