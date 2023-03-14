from django.shortcuts import render
from django.http.response import HttpResponse
from .models import InOut, PersonelList
from datetime import timedelta
import datetime

def index(request):
  if request.method=="POST":
    fromdate=request.POST.get('fromdate')
    todate=request.POST.get('todate')
    
    data=InOut.objects.raw('select * from uploadlog_inout where date between "'+fromdate+'" and "'+todate+'"')
    
    start = datetime.datetime.strptime(fromdate,"%Y-%m-%d")
    end = datetime.datetime.strptime(todate,"%Y-%m-%d")

    start_date = datetime.date(start.year,start.month,start.day)
    end_date = datetime.date(end.year,end.month,end.day)

    delta = datetime.timedelta(days=1)
    pasgecenler = []
    while start_date <= end_date:
      paslar = InOut.objects.raw('SELECT * FROM (SELECT id, personelCardNo, personelName FROM uploadlog_personellist UNION ALL SELECT id, personelCardNo, personelName FROM uploadlog_inout WHERE date BETWEEN \''+start_date.strftime("%Y-%m-%d")+'\' and \''+start_date.strftime("%Y-%m-%d")+'\') GROUP BY personelCardNo HAVING COUNT(*) = 1')
      pasTarihi = start_date.strftime("%Y-%m-%d")
      for personel in paslar:
        pasgecenler.append({'personelCardNo':personel.personelCardNo, 'personelName':personel.personelName, 'pasTarihi':pasTarihi})
      start_date += delta
    
    print(pasgecenler)
    return render(request, 'index.html', {'data':data, 'pass':pasgecenler})
  else:
    data = InOut.objects.all()
    return render(request, 'index.html', {'data': data})

def upload(request):
  return render(request, 'upload.html')