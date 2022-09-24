# Generated by Django 2.2.12 on 2022-09-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0003_auto_20220911_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='id',
        ),
        migrations.RemoveField(
            model_name='career',
            name='id',
        ),
        migrations.RemoveField(
            model_name='condition',
            name='id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.RemoveField(
            model_name='types_conditions',
            name='id',
        ),
        migrations.AlterField(
            model_name='campus',
            name='Id_campus',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='career',
            name='Id_career',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Id_condition',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Id_faculty',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='Id_group',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='Id_place',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='Id_schedule',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Id_career',
            field=models.ManyToManyField(to='Buscador.Career'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Id_subject',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='types_conditions',
            name='Id_types',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]