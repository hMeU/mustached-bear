from django.template import  RequestContext
from django.shortcuts import render

def index(request):
    client_ip = request.META['REMOTE_ADDR']
    client_os = request.META['REMOTE_HOST']
    client_browser = request.META['HTTP_USER_AGENT']
    
    context = {'addr': client_ip,
                'os': client_os,
                'browser': client_browser}

    return render(request, 'basics/index.html', context)

