# Generated by Django 2.2.12 on 2020-07-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corrida', '0028_auto_20200730_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='corrida',
            name='fecha_produccion',
            field=models.DateTimeField(null=True),
        ),
    ]