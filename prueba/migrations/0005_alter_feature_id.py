# Generated by Django 5.0.4 on 2024-04-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0004_feature_external_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
