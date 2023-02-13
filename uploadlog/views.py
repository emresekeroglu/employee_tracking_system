from django.shortcuts import render
from django.http.response import HttpResponse
from .models import InOut

def index(request):
  if request.method=="POST":
    fromdate=request.POST.get('fromdate')
    todate=request.POST.get('todate')
    data=InOut.objects.raw('select * from uploadlog_inout where date between "'+fromdate+'" and "'+todate+'"')
    return render(request, 'index.html',{"data":data})
  else:
    data = InOut.objects.all()
    return render(request, 'index.html', {'data': data})

def upload(request):
  return render(request, 'upload.html')