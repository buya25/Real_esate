# Generated by Django 3.2.12 on 2023-06-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_blog_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='position',
        ),
    ]
