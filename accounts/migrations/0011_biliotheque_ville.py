# Generated by Django 4.1.6 on 2023-02-12 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_pret_daterendu'),
    ]

    operations = [
        migrations.AddField(
            model_name='biliotheque',
            name='ville',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]