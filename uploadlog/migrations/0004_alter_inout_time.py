# Generated by Django 4.1.5 on 2023-01-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadlog', '0003_alter_inout_options_alter_personellist_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inout',
            name='time',
            field=models.TimeField(),
        ),
    ]
