# Generated by Django 2.0.7 on 2018-10-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20181016_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='investors',
            field=models.TextField(blank=True, null=True),
        ),
    ]
