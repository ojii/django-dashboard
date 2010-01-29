from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class ModerationQueue(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', related_name='objects_awaiting_approval')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')