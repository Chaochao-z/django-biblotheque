# Generated by Django 4.1.6 on 2023-02-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_pret_rendu_pret_daterendu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pret',
            name='dateend',
            field=models.DateTimeField(blank=True),
        ),
    ]
