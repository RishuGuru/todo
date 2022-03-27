# Generated by Django 4.0.3 on 2022-03-25 15:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=100, null=True)),
                ('Content', models.TextField()),
                ('Create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('Completed', models.BooleanField(default=False)),
                ('Completion_date', models.DateTimeField()),
                ('User_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='todo_app.register')),
            ],
        ),
    ]
