# Generated by Django 2.2.12 on 2022-09-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0008_auto_20220911_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Id_career',
            field=models.ManyToManyField(to='Buscador.Career'),
        ),
    ]
