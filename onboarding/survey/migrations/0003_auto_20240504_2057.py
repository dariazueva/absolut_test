# Generated by Django 3.2.16 on 2024-05-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20240503_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.survey'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
