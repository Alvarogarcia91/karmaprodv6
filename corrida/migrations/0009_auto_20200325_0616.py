# Generated by Django 2.2.4 on 2020-03-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corrida', '0008_auto_20200325_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloqueproducido',
            name='defecto',
            field=models.CharField(choices=[('sd', 'Sin defectos'), ('ph', 'Pinhole'), ('g', 'Grieta'), ('v', 'Vena'), ('mm', 'Mal manejo'), ('fdm', 'Fuera de medida'), ('a', 'Algodonozo')], default='sd', max_length=2),
        ),
        migrations.AddField(
            model_name='bloqueproducido',
            name='no_de_bloque',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bloqueproducido',
            name='revision_calidad',
            field=models.BooleanField(default=True),
        ),
    ]