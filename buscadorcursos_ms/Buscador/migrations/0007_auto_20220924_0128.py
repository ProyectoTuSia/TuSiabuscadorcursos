# Generated by Django 2.2.12 on 2022-09-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0006_auto_20220924_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Id_career',
            field=models.ManyToManyField(related_name='Materias', to='Buscador.Career'),
        ),
    ]