# Generated by Django 3.1.2 on 2021-08-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0006_auto_20210804_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='fees',
            field=models.IntegerField(blank=True, default=500),
        ),
    ]
