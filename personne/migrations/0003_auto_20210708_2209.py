# Generated by Django 3.0.8 on 2021-07-08 22:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personne', '0002_auto_20210705_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaliser',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
