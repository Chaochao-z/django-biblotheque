# Generated by Django 4.1.6 on 2023-02-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_pret_dateend_alter_pret_daterendu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pret',
            name='daterendu',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]