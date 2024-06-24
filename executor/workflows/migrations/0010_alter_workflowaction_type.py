# Generated by Django 4.1.13 on 2024-06-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0009_workflow_configuration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowaction',
            name='type',
            field=models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'API'), (2, 'SLACK_MESSAGE'), (3, 'SLACK_THREAD_REPLY'), (4, 'MS_TEAMS_MESSAGE_WEBHOOK')], db_index=True),
        ),
    ]
