# Generated by Django 2.0.6 on 2018-07-13 09:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customercare', '0003_auto_20180318_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgecenter',
            name='details',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
