# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *


# TODO: Implement some views
def index(request):
    ''' home page 
    '''
    navbar = NavBarItem.objects.filter(isActive=True)
    speakers = speakers.objects.all()
    schedule = Proposal.objects.filter(accepted=True)
    conferenceDetail = ConferenceDetail.objects.all()


    # TODO: Fix this so it's not so dangerous....
    return render(request, 'main/index.html',
                  {'speakers': speakers,
                   'schedule': schedule,
                   'banner': conferenceDetail[0],
                   'navbar': navbar})
