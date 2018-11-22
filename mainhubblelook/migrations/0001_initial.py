# Generated by Django 2.0.7 on 2018-11-19 09:55

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
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField(auto_now=True, verbose_name='Publish time')),
                ('topic', models.CharField(blank=True, max_length=2000, null=True)),
                ('micro_thought', models.CharField(blank=True, max_length=200, null=True)),
                ('Initial_keyword_for_thoughts', models.CharField(blank=True, choices=[('I think', 'I THINK'), ('Feedback', 'FEEDBACK'), ('Good part', 'GOOD PART'), ('Bad part', 'BAD PART'), ('Prototype', 'PROTOTYPE'), ('Info', 'INFO'), ('Review', 'REVIEW'), ('Ask', 'ASK'), ('Financial market', 'FINANCIAL MARKET'), ('event or happening', 'EVENT OR HAPPENING')], default='I think', max_length=300, null=True)),
                ('product_tumbline', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_title', models.CharField(blank=True, max_length=100, null=True)),
                ('launched_time', models.DateField(blank=True, null=True)),
                ('causel', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_url', models.URLField(blank=True, max_length=100, null=True)),
                ('Prices', models.IntegerField(blank=True, null=True)),
                ('product_details', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Initial_keyword_for_articles', models.CharField(blank=True, choices=[('General', 'GENERAL'), ('Product', 'PRODUCT'), ('Economics', 'ECONOMICS'), ('Market', 'MARKET'), ('Financial market', 'FINANCIAL MARKET')], default='General', max_length=10, null=True)),
                ('article_title', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('micro_article', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='UserContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('topic', models.CharField(help_text='Do not write more than 200 words', max_length=200)),
                ('write', models.TextField()),
            ],
        ),
    ]
