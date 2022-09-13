# Generated by Django 2.2.12 on 2022-09-11 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_career', models.IntegerField()),
                ('Name_career', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_condition', models.IntegerField()),
                ('Subject_condition', models.IntegerField()),
                ('Number_subject', models.IntegerField()),
                ('All_subjects', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Types_Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_types', models.CharField(max_length=5)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Conditions',
        ),
        migrations.DeleteModel(
            name='Curriculum',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='Supply_places',
            new_name='Slots',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='Id_curriculum',
            new_name='Credits',
        ),
        migrations.AddField(
            model_name='group',
            name='Id_sheduler',
            field=models.ManyToManyField(to='Buscador.Schedule'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Id_campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buscador.Campus'),
        ),
        migrations.AlterField(
            model_name='group',
            name='Id_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buscador.Subject'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='Id_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buscador.Place'),
        ),
        migrations.AddField(
            model_name='condition',
            name='Type_condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buscador.Types_Conditions'),
        ),
        migrations.AddField(
            model_name='career',
            name='Id_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buscador.Faculty'),
        ),
        migrations.AddField(
            model_name='subject',
            name='Id_career',
            field=models.ManyToManyField(to='Buscador.career'),
        ),
        migrations.AddField(
            model_name='subject',
            name='Id_condition',
            field=models.ManyToManyField(to='Buscador.Condition'),
        ),
    ]
