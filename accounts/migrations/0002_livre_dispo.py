# Generated by Django 4.1.6 on 2023-02-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='dispo',
            field=models.BooleanField(null=True),
        ),
    ]
