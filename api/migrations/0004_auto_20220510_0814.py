# Generated by Django 3.2.7 on 2022-05-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220510_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemodel',
            name='target',
        ),
        migrations.AddField(
            model_name='nmap',
            name='target',
            field=models.CharField(default='127.0.0.1', max_length=255),
        ),
        migrations.AddField(
            model_name='webcrawler',
            name='target',
            field=models.CharField(default='127.0.0.1', max_length=255),
        ),
    ]
