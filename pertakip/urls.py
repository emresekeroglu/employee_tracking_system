from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uploadlog.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

admin.site.site_header = "Personel Devam Takip Sistemi"
admin.site.site_title = "İmtek PDKS"
admin.site.index_title = "İmtek PDKS Hoş Geldiniz"