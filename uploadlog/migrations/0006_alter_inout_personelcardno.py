# Generated by Django 4.1.5 on 2023-01-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadlog', '0005_remove_inout_personel_inout_personelcardno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inout',
            name='personelCardNo',
            field=models.IntegerField(default=0),
        ),
    ]
