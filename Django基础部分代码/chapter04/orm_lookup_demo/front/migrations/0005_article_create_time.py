# Generated by Django 2.0.2 on 2018-04-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_remove_article_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
