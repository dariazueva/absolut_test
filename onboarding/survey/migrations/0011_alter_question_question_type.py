# Generated by Django 3.2.16 on 2024-05-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_alter_textresponse_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('choice', 'Choice'), ('checkbox', 'Checkbox')], default='choice', max_length=10),
        ),
    ]
