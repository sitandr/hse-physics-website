# Generated by Django 4.0.3 on 2022-06-07 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_iframe_materialcontainer_frames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='course',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='groups',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]