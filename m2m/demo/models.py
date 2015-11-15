from django.db import models

class Software(models.Model):
    name = models.CharField(max_length=60)
    version = models.CharField(max_length=10)
    programmers = models.ManyToManyField('Programmer')

    def __unicode__(self):
        return self.name

class Programmer(models.Model):
    username = models.CharField(max_length=30, primary_key=True)

    def __unicode__(self):
        return self.username