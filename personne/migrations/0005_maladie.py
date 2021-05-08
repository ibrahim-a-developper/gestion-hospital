# Generated by Django 3.0.8 on 2021-05-06 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personne', '0004_personne_prenom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personne.Personne')),
                ('date_entree', models.DateTimeField(auto_now=True)),
            ],
            bases=('personne.personne',),
        ),
    ]