# Generated by Django 4.0.3 on 2022-04-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Anesthesiology', 'Anesthesiology'), ('Pharmacy', 'Pharmacy'), ('Radiology', 'Radiology'), ('Gastroenterology', 'Gastroenterology'), ('Orthopaedics', 'Orthopaedics'), ('Community Medicine', 'Community Medicine'), ('Internal Medicine', 'Internal Medicine'), ('Laboratory', 'Laboratory'), ('Nursing', 'Nursing'), ('Medical Records', 'Medical Records'), ('Cardiology', 'Cardiology'), ('Pediatrics', 'Pediatrics'), ('Obstetics', 'Obstetics'), ('Nephrology', 'Nephrology'), ('Physiotherapy', 'Physiotherapy')], max_length=50)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='department/')),
                ('cover', models.ImageField(upload_to='department/')),
            ],
        ),
    ]
