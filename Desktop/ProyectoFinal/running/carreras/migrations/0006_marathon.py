# Generated by Django 4.0.4 on 2022-06-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0005_carrera_delete_marathon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=10, null=True)),
                ('surname', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('age', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Maraton',
                'verbose_name_plural': 'Maratons',
            },
        ),
    ]
