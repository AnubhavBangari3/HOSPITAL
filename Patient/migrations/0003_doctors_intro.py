# Generated by Django 3.1.2 on 2021-08-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20210804_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='intro',
            field=models.TextField(blank=True),
        ),
    ]