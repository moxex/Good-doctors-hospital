# Generated by Django 4.0.3 on 2022-04-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('paid', models.IntegerField(null=True)),
                ('outstanding', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('payment_type', models.CharField(choices=[('I', 'Individual'), ('C', 'Consulting')], default='I', max_length=1)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('symptoms', models.CharField(max_length=200)),
                ('prescription', models.TextField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
