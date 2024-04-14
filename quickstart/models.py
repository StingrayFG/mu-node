from django.db import models
from datetime import datetime


class Folder(models.Model):
    name = models.TextField(default='', null=True, blank=True)

    creationDate = models.DateTimeField(default=datetime.now, blank=True)
    modificationDate = models.DateTimeField(default=datetime.now, blank=True)

    uuid = models.CharField(primary_key=True, max_length=50)
    ownerUuid = models.CharField(max_length=50)
    driveUuid = models.CharField(max_length=50)
    parentUuid = models.CharField(max_length=50, null=True, blank=True)

    absolutePath = models.TextField(default='', null=True, blank=True)
    isRemoved = models.BooleanField(default=False)
    isRemovedAsChild = models.BooleanField(default=False)

class File(models.Model):
    name = models.TextField(default='', null=True, blank=True)
    name = models.IntegerField(default=0, null=True, blank=True)

    creationDate = models.DateTimeField(default=datetime.now, blank=True)
    modificationDate = models.DateTimeField(default=datetime.now, blank=True)

    uuid = models.CharField(primary_key=True, max_length=50)
    ownerUuid = models.CharField(max_length=50)
    driveUuid = models.CharField(max_length=50)
    parentUuid = models.CharField(max_length=50, null=True, blank=True)
    
    isRemoved = models.BooleanField(default=False)

