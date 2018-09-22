# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import ConferenceDetail, ConferenceLocation, ConferencePage, ConferenceSponsor, Speaker, SessionLocation, \
    Proposal, Price

# Register your models here.
# TODO: Admin Models and/or Forms
admin.site.register(ConferenceLocation)
admin.site.register(ConferencePage)
admin.site.register(ConferenceSponsor)
admin.site.register(ConferenceDetail)
admin.site.register(Speaker)
admin.site.register(SessionLocation)
admin.site.register(Proposal)
admin.site.register(Price)
