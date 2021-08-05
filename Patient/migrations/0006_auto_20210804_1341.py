# Generated by Django 3.1.2 on 2021-08-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0005_doctors_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='specialization',
            field=models.CharField(blank=True, choices=[('Cardiologists', 'Cardiologists'), ('Immunologists', 'Immunologists'), ('Ophthalmologists', 'Ophthalmologists'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Physicians', 'Physicians'), ('Gastroenterologists', 'Gastroenterologists'), ('Hematologists', 'Hematologists'), ('Infectious Disease Specialists', 'Infectious Disease Specialists'), ('Nephrologists', 'Nephrologists'), ('Neurologists', 'Neurologists'), ('Gynecologists', 'Gynecologists')], max_length=255, null=True),
        ),
    ]