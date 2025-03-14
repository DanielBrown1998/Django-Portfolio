# Generated by Django 5.1.7 on 2025-03-13 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_project_tecnology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tecnology',
            field=models.CharField(blank=True, choices=[('DJANGO', 'django.svg'), ('PYTHON', 'python.svg'), ('DART', 'dart.svg'), ('FLUTTER', 'flutter.svg'), ('CSS', 'css.svg'), ('JAVASCRIPT', 'javascript.svg'), ('POSTGRESQL', 'postgresql.svg')], default='django.svg', max_length=20),
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='ANONIMOUS', max_length=50)),
                ('text', models.TextField(max_length=500)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.project')),
            ],
        ),
    ]
