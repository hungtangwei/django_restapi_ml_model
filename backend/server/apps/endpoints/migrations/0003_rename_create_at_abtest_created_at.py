# Generated by Django 3.2.4 on 2021-06-24 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_abtest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abtest',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
