# Generated by Django 2.2.4 on 2022-04-05 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Log_Reg', '0002_logreg_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logreg',
            name='conf_password',
        ),
    ]