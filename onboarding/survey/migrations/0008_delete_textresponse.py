# Generated by Django 3.2.16 on 2024-05-19 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_textresponse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TextResponse',
        ),
    ]