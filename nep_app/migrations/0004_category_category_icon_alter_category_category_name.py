# Generated by Django 5.1 on 2024-08-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0003_rename_categorie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_icon',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
