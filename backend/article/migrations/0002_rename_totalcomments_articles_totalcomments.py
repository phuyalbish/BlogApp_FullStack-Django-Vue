# Generated by Django 5.0.6 on 2024-05-16 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='totalComments',
            new_name='totalcomments',
        ),
    ]
