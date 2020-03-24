from django.shortcuts import render, redirect
from django.views.generic import View
from resp.forms import Inputs
import requests
import time
import json
import webbrowser


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
            url = request.POST['dominio']
            destination = url
            if form.data['ip'] !='':
                ip = 'http://'+request.POST['ip']
                destination = ip
            before = time.time()
            r = requests.get(destination)
            responseTime = round((time.time() - before) * 1000)
            webbrowser.open_new_tab(destination)
            if r.history:
                print("Request was redirected")
                for resp in r.history:
                    print(resp.status_code, resp.url)
                    print("Final destination:\n{} {}".format(r.status_code, r.url))
                rdict = dict(status_code=r.history[0].status_code, time='{}ms'.format(responseTime))
            else:
                print("Request was not redirected")
                rdict = dict(status_code=r.status_code, time='{}ms'.format(responseTime))
        rjson = json.dumps(rdict)
        context = {
            'rjson': rjson,
            'destination': r.url,
            'get': True
        }
        return render(request, 'home.html', context)

