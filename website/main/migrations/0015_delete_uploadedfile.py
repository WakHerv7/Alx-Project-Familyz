# Generated by Django 4.1.3 on 2023-01-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_uploadedfile_individu_photoname_individu_photopath'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
