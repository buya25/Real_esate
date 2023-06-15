import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    # Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

    def add_title(self, title):
        new_title = Title.objects.create(title=title, category=self)
        return new_title


class Title(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='listings')
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    area = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    HOUSE_STATUS_CHOICES = [
        ('rent', 'Rent'),
        ('sale', 'Sale'),
    ]
    house_status = models.CharField(max_length=10, choices=HOUSE_STATUS_CHOICES, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    square_feet = models.PositiveIntegerField(default=0)
    amount = models.CharField(max_length=200, null=True, blank=True)
    near_location = models.CharField(max_length=200, null=True, blank=True)

    # ImageFields
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg',
                                    upload_to='square')
    landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg',
                                  upload_to='landscape')
    tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg',
                                  upload_to='tall')

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('property-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Title, self).save(*args, **kwargs)


class Client(models.Model):
    user_name = models.CharField(max_length=200, null=True, blank=True, default='Anonymous')
    email = models.EmailField(null=True, blank=True, default='')
    phone_number = models.CharField(max_length=20, null=True, blank=True, default='')
    comments = models.TextField(null=True, blank=True, default='')
    job_title = models.CharField(max_length=200, null=True, blank=True, default='')
    job_desc = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.user_name


class Agents(models.Model):
    name = models.CharField(max_length=200, default='Agent')
    description = models.TextField(default='')
    profile_image = models.ImageField(upload_to='agents', default='default_profile.jpg')
    twitter_link = models.URLField(blank=True, default='#')
    facebook_link = models.URLField(blank=True, default='#')
    instagram_link = models.URLField(blank=True, default='#')
    youtube_link = models.URLField(blank=True, default='#')

    def __str__(self):
        return self.name


class Blog(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=100, default='Anonymous')
    content = models.TextField(default='')
    publication_date = models.DateField(default=timezone.now)
    categories = models.ManyToManyField('Category', default=None)
    featured_image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg',
                                       upload_to='square')
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    related_blogs = models.ManyToManyField('self', blank=True)
    is_published = models.BooleanField(default=False)

    def update_comments_count(self):
        self.comments = self.blog_comments.count()
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        self.last_updated = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    user_name = models.CharField(max_length=200, default='')
    comment_text = models.TextField(default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the comment first

        # Update the comments count for the associated blog
        self.blog.update_comments_count()

        # Update the parent blog's last_updated field
        self.blog.last_updated = self.pub_date
        self.blog.save()

    def __str__(self):
        return f"{self.user_name} on {self.blog.title}"
