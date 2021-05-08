# Generated by Django 3.0.8 on 2021-05-05 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personne', '0001_initial'),
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
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Code')),
                ('nom_service', models.CharField(max_length=20)),
                ('batiment', models.CharField(max_length=20)),
                ('directeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directeur_service', to='personne.Docteur')),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_salle', models.IntegerField(max_length=20)),
                ('nom_infermier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salle_infermier', to='personne.Infermier')),
                ('nom_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salle_service', to='hopital.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitaliser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_lit', models.IntegerField(max_length=20)),
                ('diagnostic', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('nom_maladie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitaliser_maladie', to='hopital.Maladie')),
                ('nom_salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitaliser_salle', to='hopital.Salle')),
            ],
        ),
    ]
