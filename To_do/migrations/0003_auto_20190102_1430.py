# Generated by Django 2.1.4 on 2019-01-02 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('To_do', '0002_auto_20190102_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_text',
            new_name='text',
        ),
    ]
