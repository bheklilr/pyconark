# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from redactor.fields import RedactorField


''' Models for Conference Website
'''

class ConferenceLocation(models.Model):
    ''' locations are places where events are held.
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
    ''' details about our conference.
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
    ''' pages contain all the info for a page to be created.
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

class Speaker(models.Model):
    ''' conference speakers 
    '''
    first_name   = models.CharField(max_length=250)
    last_name    = models.CharField(max_length=255)
    description  = models.TextField()
    img          = models.ImageField()
    slug         = models.SlugField()
    phone        = models.CharField(max_length=20, null=True, blank=True)
    email        = models.EmailField()
    facebook     = models.URLField()
    twitter      = models.URLField()
    github       = models.URLField()
    linkedin     = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify("{} {}".format(self.first_name, self.last_name))
        super(Speaker, self).save(*args, **kwargs)

class SessionLocation(models.Model):
    ''' session location
            these are where talks will be held.
    '''
    room_name = models.CharField(max_length=255)
    building  = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {}".format(self.building, self.room_name)

    def __str__(self):
        return "{} {}".format(self.building, self.room_name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify("{} {}".format(self.building, self.room_name))
        super(SessionLocation, self).save(*args, **kwargs)

class Proposal(models.Model):
    ''' proposal 
            can be marked as a session with the 'accepted' flag
            can associate to a session location
    '''
    title            = models.CharField(max_length=255)
    slug             = models.SlugField()
    description      = models.TextField()
    speaker          = models.ForeignKey(Speaker)
    accepted         = models.BooleanField(default=False)
    session_location = models.ForeignKey(SessionLocation, null=True, blank=True)
    time             = models.TimeField()
    date_created     = models.DateTimeField(auto_now_add=True)
    last_updated     = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Proposal, self).save(*args, **kwargs)

class Price(models.Model):
    ''' conference prices
    '''
    title            = models.CharField(max_length=255)
    description      = models.TextField()
    slug             = models.SlugField()
    amount           = models.PositiveIntegerField()
    date_created     = models.DateTimeField(auto_now_add=True)
    last_updated     = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Price, self).save(*args, **kwargs)

class ConferenceSponsor(models.Model):
    ''' conference sponsor model
    '''
    slug             = models.SlugField()
    name             = models.CharField(max_length=255)
    img              = models.ImageField()
    link             = models.URLField()
    description      = models.TextField()
    date_created     = models.DateTimeField(auto_now_add=True)
    last_updated     = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Price, self).save(*args, **kwargs)