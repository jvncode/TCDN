from django.shortcuts import render, redirect
from django.views.generic import View
from resp.forms import Inputs
import requests
import time
import json
import socket


class ResponseView(View):
    
    def get(self, request):
        form = Inputs()
        context = {
            'form': form,
        }
        return render(request, 'home.html', context)
    
    def post(self, request):
        form = Inputs(request.POST)
        if form.is_valid:
            before = time.time()
            r = requests.get(form.data['dominio'], auth=('user', 'pass'))
            responseTime = time.time() - before
            rdict = dict(status_code=r.status_code, time='{:.2f} seg'.format(responseTime))
            rjson = json.dumps(rdict)
            if form.data['ip'] !='':
                IP = form.data['ip']
                PORT = 80
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((IP,PORT))
                url = 'http://localhost/?dominio={}&ip={}'.format(form.data['dominio'], form.data['ip'])
            else:
                url = 'http://localhost/?dominio={}'.format(form.data['dominio'])
        context = {
            'form': form,
            'rjson': rjson,
            'url': url
        }
        return render(request, 'home.html', context)

