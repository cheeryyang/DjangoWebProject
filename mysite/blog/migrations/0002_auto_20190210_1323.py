# Generated by Django 2.1.3 on 2019-02-10 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='created',
        ),
    ]
