# Generated by Django 2.2.4 on 2022-04-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.CharField(max_length=45),
        ),
    ]
