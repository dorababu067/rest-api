# Generated by Django 3.0.4 on 2020-03-17 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]
