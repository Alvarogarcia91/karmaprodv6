# Generated by Django 2.2.4 on 2020-04-30 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corrida', '0019_elementocorrida_lote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloqueproducido',
            name='alto_caliente',
        ),
        migrations.RemoveField(
            model_name='bloqueproducido',
            name='ancho_caliente',
        ),
        migrations.RemoveField(
            model_name='bloqueproducido',
            name='flujo_de_aire_caliente',
        ),
    ]
