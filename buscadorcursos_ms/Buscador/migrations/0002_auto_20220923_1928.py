# Generated by Django 2.2.12 on 2022-09-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='Id_faculty',
        ),
        migrations.AddField(
            model_name='group',
            name='Id_faculty',
            field=models.ManyToManyField(to='Buscador.Faculty'),
        ),
    ]