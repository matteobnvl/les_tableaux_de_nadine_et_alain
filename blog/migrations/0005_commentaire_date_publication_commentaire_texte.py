# Generated by Django 4.0.6 on 2022-07-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_tableau_photo_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='date_publication',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='texte',
            field=models.TextField(null=True),
        ),
    ]
