# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render

from basic.models import Index
from django.http import HttpResponse, HttpResponseRedirect
import json


def index(request):
    # context = {}
    store = Index.objects.all()
    # context["items"] = product
    loggedIn = False
    if request.session.has_key('username'):
        loggedIn = True
    # store = Heels.objects.all()
    print(store)

    for store_vsl in store:
        print(store_vsl.price)
        print(store_vsl.img1)
        print(store_vsl.BrandName)

        print(store_vsl.store)
    return render(request, 'index.html', {'stores': store})


def add(request):
    print('In the add method.')
    if request.method == 'POST':
        print('In the post method.')
        # print(request.body)
        # body_unicode = request.body.decode('utf-8')
        # request_body = json.loads(body_unicode)
        request_body = dict(request.POST.lists())
        print(type(request_body))
        print(request_body)
        print(request_body.get("brand")[0])
        scooter = Index(BrandName=request_body.get("brand")[0],
                        BikeName=request_body.get("bike")[0],
                        img=request_body.get("img")[0],
                        img1=request_body.get("img1")[0], store=request_body.get("store")[0],
                        price=request_body.get("price")[0])

        scooter.save()
        return HttpResponseRedirect('/')

    return render(request, 'add.html')
