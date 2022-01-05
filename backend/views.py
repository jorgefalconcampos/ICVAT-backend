import os
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse



TEMPLATES_DIR =  settings.TEMPLATES_DIR #importing



def index(request):
    """Main entry point of the app"""
    return HttpResponse("Hello")



def page_not_found_view(request, exception):
    template = TEMPLATES_DIR / 'http_states' / '404.html'

    return render(request, template, status=404)