# Generated by Django 2.2.12 on 2022-09-23 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0002_auto_20220923_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='Id_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buscador.Place'),
        ),
    ]
