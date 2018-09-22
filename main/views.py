# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ConferenceDetail


# TODO: Implement some views
def index(request):
    ''' home page '''
    speakers = []
    speakers.append({
        "name": "BOB JOHNSON",
        "company": "Initech",
        "phone": "1234567890",
        "bio": "A short description about the speaker's background and qualifications",
        "email": "email@domain.com"
    })
    speakers.append({
        "name": "Wally West",
        "company": "Star Labs",
        "phone": "1234567890",
        "bio": "This guy runs really fast. He's famous, and never screws up the timeline by time traveling.",
        "email": "email@domain.com"
    })
    schedule = []
    schedule.append({
        "title": "TITLE",
        "name": "NAME",
        "room": "ROOM",
        "time": "TIME"
    })
    schedule.append({
        "title": "TITLE",
        "name": "NAME",
        "room": "ROOM",
        "time": "TIME"
    })
    conferenceDetail = ConferenceDetail.objects.all()
    conferenceDetail[0]
    return render(request, 'main/index.html',
                  {'speakers': speakers, 'schedule': schedule, 'banner': conferenceDetail[0]})
