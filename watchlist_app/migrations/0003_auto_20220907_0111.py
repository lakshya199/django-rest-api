# Generated by Django 3.2.14 on 2022-09-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_auto_20220907_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Directorname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='movie',
            name='website',
            field=models.URLField(max_length=100),
        ),
    ]
