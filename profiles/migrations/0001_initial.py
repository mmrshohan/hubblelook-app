# Generated by Django 2.0.7 on 2018-11-16 08:46

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficalLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('to_whom', models.CharField(blank=True, max_length=300, null=True)),
                ('letter', ckeditor.fields.RichTextField()),
                ('pub_time', models.DateTimeField(auto_now=True, verbose_name='Publish time')),
                ('letter_from', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_of_account', models.NullBooleanField(help_text='by default this is Business account', verbose_name='Personal account')),
                ('user_photo', models.ImageField(blank=True, upload_to='user_image')),
                ('occupation', models.CharField(max_length=400)),
                ('name', models.CharField(default=None, max_length=200)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('additional_url', models.URLField(blank=True, null=True)),
                ('Headquarter', models.CharField(blank=True, max_length=1000, null=True)),
                ('stock_market', models.CharField(blank=True, max_length=200, null=True)),
                ('established', models.DateField(default=None)),
                ('investors', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('about_details', ckeditor.fields.RichTextField(default=None)),
                ('Type_of_company', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private'), ('Initiative', 'Initiative'), ('Private and Startup', 'Private and Startup')], default='Private and Startup', max_length=20, null=True)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1200, null=True)),
                ('team', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
