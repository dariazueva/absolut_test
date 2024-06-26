# Generated by Django 3.2.16 on 2024-05-19 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_question_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_responses', to='survey.question')),
            ],
        ),
    ]
