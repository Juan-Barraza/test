# Generated by Django 5.0.4 on 2024-04-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='external_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
