# Generated by Django 3.1.2 on 2021-08-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0008_remove_doctors_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='fees',
            field=models.IntegerField(default=500),
        ),
    ]
