# Generated by Django 5.1 on 2024-09-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0017_alter_image_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_slider',
            name='image',
            field=models.ImageField(upload_to='slider/'),
        ),
    ]