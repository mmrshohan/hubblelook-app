# Generated by Django 2.0.6 on 2018-07-23 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]