from datetime import datetime
from time import strftime, strptime
from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import render
from .models import InOut,PersonelList
from django import forms
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter

class CsvImportForm(forms.Form):
  csv_upload = forms.FileField()

class PersonelListAdmin(admin.ModelAdmin):
  list_display = ('personelName','personelCardNo')
  search_fields = ('personelName','personelCardNo')
  
class InOutAdmin(admin.ModelAdmin):
  list_display = ('personelName','personelCardNo','time','date','girisCikis', 'notlar')
  search_fields = ('personelName','date','girisCikis')
  list_filter = (('date', DateRangeFilter),)
  
  def get_urls(self):
    urls = super().get_urls()
    new_urls = [path('upload-csv/', self.upload_csv),]
    return new_urls + urls
  
  def upload_csv(self, request):
    if request.method == "POST":
      csv_file = request.FILES["csv_upload"]
      file_data = csv_file.read().decode("utf-8")
      csv_data = file_data.split("\n")
      
      i = 0
      for x in csv_data:
        i += 1
        if i == len(csv_data):
          break
        fields = x.split(",")
        tarih=fields[2].replace('\r','')
        tarih= tarih[:2]+'.'+tarih[2:4]+'.20'+tarih[4:]
        
        try:
          perName = PersonelList.objects.get(personelCardNo = fields[0]).personelName
        except ObjectDoesNotExist:
          perName = 'Yeni Personel Kartı Tanımlanmamış'
        
        if fields[1] > '17:30':
            girCik = "ÇIKIŞ"
        elif fields[1] > '07:00' and fields[1] <= '08:05':
          girCik = "GİRİŞ"
        elif fields[1] >= '08:06' and fields[1] < '09:00':
          girCik = "GEÇ GİRİŞ"
        elif fields[1] > '17:30':
          girCik = "ÇIKIŞ"
        elif fields[1] <= '17:30' and fields[1] > '10:00':
          girCik = "ERKEN ÇIKIŞ" 
        else:
          girCik = "GİRİŞ"
            
        created = InOut.objects.update_or_create(
          personelCardNo = fields[0],
          personelName = perName,
          time = fields[1],
          date = datetime.strptime(tarih,'%d.%m.%Y'),
          girisCikis = girCik
        )
      url = reverse('admin:index')
      return HttpResponseRedirect(url)

    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)
  
admin.site.register(InOut,InOutAdmin)
admin.site.register(PersonelList,PersonelListAdmin)