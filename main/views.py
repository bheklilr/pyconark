# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# TODO: Implement some views
def index(request):
    ''' home page '''
    speakers = []
    speakers.append({
        "name": "BOB JOHNSON",
        "contact": "1234567890",
        "description": "email@domain.com"
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

    return render(request, 'main/index.html', {'speakers': speakers, 'schedule': schedule})
