# Generated by Django 4.1.3 on 2022-11-16 05:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_workdetailspage_workindexpage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='creator_description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=ckeditor.fields.RichTextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='blog_description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='workdetailspage',
            name='work_description',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='workindexpage',
            name='intro',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
