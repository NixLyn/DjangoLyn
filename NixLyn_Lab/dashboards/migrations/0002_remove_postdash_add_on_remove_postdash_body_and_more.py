# Generated by Django 4.2 on 2023-04-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdash',
            name='add_on',
        ),
        migrations.RemoveField(
            model_name='postdash',
            name='body',
        ),
        migrations.RemoveField(
            model_name='postdash',
            name='color',
        ),
        migrations.RemoveField(
            model_name='postdash',
            name='date_made',
        ),
        migrations.RemoveField(
            model_name='postdash',
            name='title',
        ),
    ]