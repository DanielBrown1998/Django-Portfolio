# Generated by Django 5.1.7 on 2025-03-13 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_project_tecnology'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=None, upload_to='image/<django.db.models.fields.CharField>'),
        ),
    ]
