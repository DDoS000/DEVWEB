from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

from .models import Portfolio,Contacts
from datetime import date

# Create your views here.
def index(req):
    if req.method == 'POST':
        post = req.POST
        s = Contacts()
        s.name = post['name']
        s.email = post['email']
        s.phone = post['phone']
        s.mess = post['message']
        s.time = date.today()
        s.save()
        Portfolios = Portfolio.objects.all()
        return render(req, 'myapp/index.html', { 'Portfolios': Portfolios })
    else:
        Portfolios = Portfolio.objects.all()
        return render(req, 'myapp/index.html' , { 'Portfolios': Portfolios })
    # if req.method == 'POST':
    #     post = req.POST
    #     s = Service()
    #     s.icon = post['icon']
    #     s.title = post['title']
    #     s.detail = date.today()
    #     s.save()
    #     services = Service.objects.all()
    #     print(services)
    #     return render(req, 'myapp/index.html', { 'services': services })
    # else:
    #     print('ร้องขอทำมะดา')
    #     services = Service.objects.all()
    #     print(services)
    #     return render(req, 'myapp/index.html', { 'services': services })
    # if req.method == 'message':
    #     return render(req, 'myapp/message.html')

def dev(req):
    if req.method == 'POST':
        post = req.POST
        p = Portfolio()
        p.title = post['title']
        p.detail = post['detail']
        p.photo = post['photo']
        p.url = post['url']
        p.save()
        Contact = Contacts.objects.all()
        return render(req, 'myapp/dev.html', { 'Contact': Contact })
    else:
        Contact = Contacts.objects.all()
        return render(req, 'myapp/dev.html', { 'Contact': Contact })