# Generated by Django 2.0.7 on 2018-11-19 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainhubblelook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]