# Generated by Django 2.2.12 on 2022-09-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0004_auto_20220911_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Id_career',
            field=models.ManyToManyField(to='Buscador.Career'),
        ),
    ]