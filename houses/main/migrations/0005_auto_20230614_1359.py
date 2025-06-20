# Generated by Django 3.2.12 on 2023-06-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_blog_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(default=None, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publication_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
