# Generated by Django 4.0.3 on 2022-03-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]