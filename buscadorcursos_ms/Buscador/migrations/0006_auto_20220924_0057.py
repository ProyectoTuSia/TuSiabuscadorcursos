# Generated by Django 2.2.12 on 2022-09-24 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0005_auto_20220923_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='Id_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Careers', to='Buscador.Faculty'),
        ),
    ]
