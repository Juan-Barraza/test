# Generated by Django 5.0.4 on 2024-04-08 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=100, unique=True)),
                ('magnitude', models.FloatField()),
                ('place', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('tsunami', models.BooleanField()),
                ('mag_type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='prueba.feature')),
            ],
        ),
    ]
