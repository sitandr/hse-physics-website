# Generated by Django 4.0.3 on 2022-05-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_material_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_material',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]