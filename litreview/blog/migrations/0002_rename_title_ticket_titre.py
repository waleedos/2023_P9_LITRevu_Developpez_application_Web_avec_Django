# Generated by Django 4.2 on 2023-08-01 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='title',
            new_name='titre',
        ),
    ]
