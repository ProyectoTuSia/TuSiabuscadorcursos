# Generated by Django 2.2.12 on 2022-09-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0016_auto_20220913_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Id_career',
            field=models.ManyToManyField(to='Buscador.Career'),
        ),
    ]