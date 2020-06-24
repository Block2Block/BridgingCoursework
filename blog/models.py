# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    full_body = models.TextField()
    short_body = models.TextField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
