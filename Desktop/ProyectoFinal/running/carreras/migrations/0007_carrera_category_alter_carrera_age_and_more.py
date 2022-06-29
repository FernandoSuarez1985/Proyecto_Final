# Generated by Django 4.0.4 on 2022-06-29 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0006_marathon'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carreras', to='carreras.marathon'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrera',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='marathon',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='marathon',
            name='number',
            field=models.CharField(max_length=50),
        ),
    ]
