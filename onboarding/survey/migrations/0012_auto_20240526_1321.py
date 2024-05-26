# Generated by Django 3.2.16 on 2024-05-26 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_alter_question_question_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('question',), 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='textresponse',
            options={'ordering': ('question',), 'verbose_name': 'Текстовый ответ', 'verbose_name_plural': 'Текстовые ответы'},
        ),
        migrations.CreateModel(
            name='CheckboxResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question')),
            ],
            options={
                'verbose_name': 'Ответ с галочкой',
                'verbose_name_plural': 'Ответы с галочкой',
                'ordering': ('question',),
            },
        ),
    ]