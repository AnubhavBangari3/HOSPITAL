# Generated by Django 3.1.2 on 2021-08-04 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fees', models.IntegerField(default=500)),
                ('specialization', models.ManyToManyField(to='Patient.Diseases')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='Patient.diseases')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_name', to='Patient.doctors')),
                ('fees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_fees', to='Patient.doctors')),
            ],
        ),
    ]
