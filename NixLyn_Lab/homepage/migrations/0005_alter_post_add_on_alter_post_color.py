# Generated by Django 4.2 on 2023-04-10 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_post_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='add_on',
            field=models.CharField(default='SideNote: ', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(default='blue', max_length=50),
        ),
    ]