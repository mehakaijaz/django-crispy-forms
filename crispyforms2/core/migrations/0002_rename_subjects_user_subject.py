# Generated by Django 5.0.6 on 2024-05-13 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='subjects',
            new_name='subject',
        ),
    ]