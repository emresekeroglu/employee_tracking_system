# Generated by Django 4.1.5 on 2023-01-26 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadlog', '0002_inout_personel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inout',
            options={'verbose_name': 'Giriş Çıkış Kaydı', 'verbose_name_plural': 'Giriş Çıkış Kayıtları'},
        ),
        migrations.AlterModelOptions(
            name='personellist',
            options={'verbose_name': 'Personel', 'verbose_name_plural': 'Personel Listesi'},
        ),
        migrations.RemoveField(
            model_name='inout',
            name='personelCardNo',
        ),
    ]
