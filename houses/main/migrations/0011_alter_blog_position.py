# Generated by Django 3.2.12 on 2023-06-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_blog_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='position',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
