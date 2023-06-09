# Generated by Django 4.0.6 on 2022-07-20 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peintre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('description_peintre', models.CharField(help_text='Entrer description sur vous', max_length=250)),
            ],
            options={
                'ordering': ['nom', 'prenom'],
            },
        ),
        migrations.CreateModel(
            name='Tableau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tableau', models.CharField(help_text='Entrer un nom de tableau', max_length=200)),
                ('description', models.CharField(help_text='Entrer la description du tableau', max_length=250)),
                ('longueur', models.CharField(help_text='Entrer la longueur du tableau en centimètre', max_length=50)),
                ('largeur', models.CharField(help_text='Entrer la largeur du tabeleau en centimètre', max_length=50)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('type', models.CharField(help_text='Entrer type de peinture du tableau', max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('meilleur_realisation', models.CharField(max_length=10)),
                ('affichage', models.CharField(max_length=10)),
                ('peintre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.peintre')),
            ],
        ),
    ]
