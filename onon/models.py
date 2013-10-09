from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from datetime import datetime

class Zahltag(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    image = models.URLField()

    def __unicode__(self):
        return u'Zahltag: '+self.name

class Feature(models.Model):
    title = models.TextField()
    date = models.DateTimeField(default=lambda: datetime.now())

    main_content_type = models.ForeignKey(ContentType, related_name='featured_at')
    main_object_id = models.PositiveIntegerField()
    main_story = generic.GenericForeignKey('main_content_type', 'main_object_id')


    other_content_type = models.ForeignKey(ContentType, null=True, related_name='secondary_feature_at')
    other_object_id = models.PositiveIntegerField(null=True)
    other_story = generic.GenericForeignKey('other_content_type', 'other_object_id')

    editorial = models.TextField()

    def __unicode__(self):
        return u'Feature: %s / %s' %(self.title, self.date)

class NonfeatureContent(models.Model):
    url = models.URLField()
    text = models.TextField()
    image = models.URLField(null=True)
    date = models.DateTimeField(default=lambda: datetime.now())

    def __unicode__(self):
        return u'NFC: %s (%s) / %s' % (self.text, self.url, self.date)
