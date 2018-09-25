# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.auth.models import User
from main.models import *

import datetime

class ConferenceLocationTest(TestCase):
    ''' Conference Location Tests
    '''
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', email='test@pyark.org', password='holycowbatman')

        ConferenceLocation.objects.create(
            name = 'Test Location',
            address = '123 address street',
            city = 'Little Rock',
            state = 'AR',
            zip_code = '72201',
            phone = '501-222-1111',
            latitude = 35.233,
            longitude = -92.454,
            author = test_user
        )

    def test_name_label(self):
        conference_location = ConferenceLocation.objects.get(id=1)
        field_label = conference_location._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_location_has_author(self):
        conference_location = ConferenceLocation.objects.get(id=1)
        author = conference_location.author
        self.assertTrue(author != None)


class ConferenceDetailTest(TestCase):
    ''' Conference Detail Tests
    '''
    @classmethod
    def setUpTestData(cls):
        start_dt = datetime.datetime.strptime("09/25/2018", "%m/%d/%Y")
        end_dt = start_dt + datetime.timedelta(days=5)

        test_user = User.objects.create_user(
            username='testuser',
            email='test@pyark.org', 
            password='holycowbatman'
        )

        test_location = ConferenceLocation.objects.create(
            name = 'Test Location',
            address = '123 address street',
            city = 'Little Rock',
            state = 'AR',
            zip_code = '72201',
            phone = '501-222-1111',
            latitude = 35.233,
            longitude = -92.454,
            author = test_user
        )


        ConferenceDetail.objects.create(
            title = 'Test Location',
            location = test_location,
            start_dt = start_dt,
            end_dt = end_dt
        )
    
    def test_start_dt_label(self):
        conference_detail = ConferenceDetail.objects.get(id=1)
        field_label = conference_detail._meta.get_field('start_dt').verbose_name
        self.assertEquals(field_label, "Start Date/Time")

    def test_end_dt_label(self):
        conference_detail = ConferenceDetail.objects.get(id=1)
        field_label = conference_detail._meta.get_field('end_dt').verbose_name
        self.assertEquals(field_label, "End Date/Time")


class ConferencePageTest(TestCase):
    ''' Conference Page Tests
    '''
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser',
            email='test@pyark.org', 
            password='holycowbatman'
        )


        ConferencePage.objects.create(
            title = 'Test Page',
            introduction = 'my test introduction',
            body = "<b>Here is some bod with html in it</b>",
            sidebar = None,
            author = test_user
        )
    
    def test_page_slug(self):
        conference_page = ConferencePage.objects.get(id=1)
        self.assertEquals(conference_page.slug, "test-page")

    def test_body_has_html(self):
        conference_page = ConferencePage.objects.get(id=1)
        self.assertInHTML("Here is some bod with html in it", conference_page.body)

