# Generated by Django 2.0.6 on 2018-08-12 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainhubblelook', '0002_quickword_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quickword',
            name='user',
            field=models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
