# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def social(request):
    return render(request, "social/social.html", {'url': "social"})
