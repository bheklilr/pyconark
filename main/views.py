# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    ''' home page '''
    return render(request, 'main/index.html', {})