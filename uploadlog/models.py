from django.db import models

class PersonelList(models.Model):
  personelCardNo = models.IntegerField("Kart No")
  personelName = models.CharField("Ad Soyad",max_length=200)
  
  def __str__(self):
    return f"{self.personelName}, {self.personelCardNo}"
  
  class Meta:
    verbose_name = 'Personel'
    verbose_name_plural = 'Personel Listesi'

class InOut(models.Model):
  personelCardNo = models.IntegerField("Kart No",default=0000)
  personelName = models.CharField("Ad Soyad",default='', max_length=250)
  time = models.TimeField("Saat")
  date = models.DateField("Tarih")
  girisCikis = models.CharField("Durum",default='' ,max_length=25)
  notlar = models.CharField("Not", blank=True, null=True, max_length=250)
  
  def __str__(self):
    return f"{self.personelCardNo}"
  
  class Meta:
    verbose_name = 'Giriş Çıkış Kaydı'
    verbose_name_plural = 'Giriş Çıkış Kayıtları'