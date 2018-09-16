# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from redactor.fields import RedactorField

'''
    Models for Conference Website
'''

class ConferenceLocation(models.Model):
    '''Locations are places where events are held.
    '''
    name         = models.CharField(max_length=120)
    address      = models.CharField(max_length=120)
    city 		 = models.CharField(max_length=120)
    state 	  	 = models.CharField(max_length=2, default='AR')
    zip_code 	 = models.CharField(max_length=5)
    phone		 = models.CharField(max_length=20, null=True, blank=True)
    fax			 = models.CharField(max_length=20, null=True, blank=True)
    latitude	 = models.FloatField(null=True, blank=True)
    longitude	 = models.FloatField(null=True, blank=True)
    author 		 = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ConferenceDetail(models.Model):
    '''Details about our conference.
    '''
    title        = models.CharField(max_length=200)
    location = models.ForeignKey(ConferenceLocation)
    start_dt 	 = models.DateTimeField(verbose_name='Start Date/Time')
    end_dt 	 	 = models.DateTimeField(null=True,blank=True,verbose_name='End Date/Time')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class ConferencePage(models.Model):
    '''Pages contain all the info for a page to be created.
    '''
    title 		 = models.CharField(max_length=120)
    introduction = models.CharField(max_length=255,null=True,blank=True)
    body 		 = RedactorField(verbose_name='body', upload_to='page_body')
    sidebar 	 = RedactorField(verbose_name='sidebar', null=True, blank=True, upload_to='page_sidebar_body')
    author 		 = models.ForeignKey(User)
    slug         = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # saving the slug everytime from the title
        self.slug = slugify(self.title)
        super(ConferencePage, self).save(*args, **kwargs)
