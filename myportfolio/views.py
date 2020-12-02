from django.http import HttpResponse
from django.shortcuts import render

from django.template import RequestContext

def base(request):

    return render(request,'base.html')

def handler404page(request,exception):
    return render(request, '404.html', status=404)



