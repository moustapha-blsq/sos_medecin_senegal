from curses.ascii import HT
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse
from . models import Personnel
from django.template import loader
from django.http import HttpResponse
# Create your views here. 
def liste_clients(request, id):
    personnel=Personnel.objects.get(id=id)
    context={'personnel', personnel}
    tempate = loader.get_template('personnel/list_client.html')
    return HttpResponse(tempate.render(context, request))
    #return render(request, , context)
   # render_to_string('personnel/list_client.html', context)
   