# Generated by Django 4.0.3 on 2022-04-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_emailuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='role',
            field=models.TextField(choices=[('', 'Аноним '), ('Преподаватель', 'Преподаватель'), ('Студент', 'Студент')], default='', max_length=30),
        ),
    ]