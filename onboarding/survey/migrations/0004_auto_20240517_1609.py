# Generated by Django 3.2.16 on 2024-05-17 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20240504_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionbranch',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='questionbranch',
            name='next_question',
        ),
        migrations.RemoveField(
            model_name='questionbranch',
            name='question',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='business_direction',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='business_type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='dynamic',
        ),
        migrations.RemoveField(
            model_name='question',
            name='parent_question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='survey',
        ),
        migrations.AddField(
            model_name='answer',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers_to_next', to='survey.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_question', to='survey.question'),
        ),
        migrations.DeleteModel(
            name='BusinessDirection',
        ),
        migrations.DeleteModel(
            name='BusinessType',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='QuestionBranch',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]
