# Generated by Django 3.2.16 on 2024-05-18 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20240517_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='next_question',
        ),
    ]
