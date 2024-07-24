# Generated by Django 4.1.13 on 2024-07-23 15:59

from django.db import migrations
from hashlib import md5


def transform_logs_task_execution_task(apps, schema_editor):
    PlayBookTaskExecutionLog = apps.get_model("executor", "PlayBookTaskExecutionLog")

    for db_task in PlayBookTaskExecutionLog.objects.filter(playbook_task_result__type="LOGS"):
        try:
            task_result = db_task.playbook_task_result
            task_table_result = task_result.get('table', {})
            if task_table_result:
                task_result['logs'] = task_table_result
                task_result.pop('table')
                db_task.save()
        except Exception as e:
            print('skip task transformation for task id: ', db_task.id)
            print(f"Error transforming task {db_task.id}: {e}")
            continue


class Migration(migrations.Migration):
    dependencies = [
        ('executor', '0042_playbooktaskexecutionlog_execution_global_variable_set'),
    ]

    operations = [
        migrations.RunPython(transform_logs_task_execution_task, migrations.RunPython.noop)
    ]
