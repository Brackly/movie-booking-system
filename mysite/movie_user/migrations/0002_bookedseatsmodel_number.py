# Generated by Django 3.1.5 on 2021-02-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedseatsmodel',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]