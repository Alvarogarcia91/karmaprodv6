# Generated by Django 2.2.4 on 2020-04-29 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espumas', '0005_auto_20200429_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloquemedidas',
            name='stock',
        ),
    ]