# Generated by Django 4.1.2 on 2022-11-09 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_topic_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='published',
        ),
    ]
