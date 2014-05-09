from django.template import  RequestContext
from django.shortcuts import render
from basics.models import IP

import httpagentparser

def index(request):
    p = IP();

    p.addr = request.META['REMOTE_ADDR']
    s = httpagentparser.simple_detect(request.META['HTTP_USER_AGENT'])
    p.browser = s[0]
    p.os = s[1]
    
    context = {
        'addr': p.addr,
        'os':p.os,
        'browser': p.browser
    }

    p.save()

    return render(request, 'basics/index.html', context)
    