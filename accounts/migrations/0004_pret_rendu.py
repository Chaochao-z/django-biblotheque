# Generated by Django 4.1.6 on 2023-02-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_livre_dispo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pret',
            name='rendu',
            field=models.BooleanField(default=False),
        ),
    ]
