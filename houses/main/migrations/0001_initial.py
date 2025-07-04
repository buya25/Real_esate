# Generated by Django 3.2.12 on 2023-06-14 09:24

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, default='Anonymous', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('comments', models.TextField(blank=True, default='', null=True)),
                ('job_title', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('job_desc', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('bedrooms', models.PositiveIntegerField(default=0)),
                ('bathrooms', models.PositiveIntegerField(default=0)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('house_status', models.CharField(blank=True, choices=[('rent', 'Rent'), ('sale', 'Sale')], max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('altText', models.TextField(blank=True, null=True)),
                ('hashtags', models.CharField(blank=True, max_length=300, null=True)),
                ('square_feet', models.PositiveIntegerField(default=0)),
                ('amount', models.CharField(blank=True, max_length=200, null=True)),
                ('near_location', models.CharField(blank=True, max_length=200, null=True)),
                ('squareImage', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_square.jpg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='square')),
                ('landImage', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_land.jpg', force_format=None, keep_meta=True, quality=75, scale=None, size=[2878, 1618], upload_to='landscape')),
                ('tallImage', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1618, 2878], upload_to='tall')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='main.category')),
            ],
        ),
    ]
