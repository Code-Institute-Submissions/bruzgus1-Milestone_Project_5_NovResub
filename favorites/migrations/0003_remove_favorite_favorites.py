# Generated by Django 4.1.1 on 2022-10-25 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0002_favorite_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='favorites',
        ),
    ]
