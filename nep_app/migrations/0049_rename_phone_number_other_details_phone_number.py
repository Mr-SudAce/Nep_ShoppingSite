# Generated by Django 5.1 on 2024-11-16 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0048_other_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='other_details',
            old_name='phone_number',
            new_name='Phone_number',
        ),
    ]
