from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

    
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES=(
		('draft','Draft'),
		('published','Published'),
		)
	tittle  = models.CharField(max_length=250)
	slug    = models.SlugField(max_length=250,unique_for_date = 'publish')
	author  = models.ForeignKey(User, related_name='blog_posts')
	body    = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add =True)
	updated = models.DateTimeField(auto_now=True)
	status  = models.CharField(max_length = 10, choices=STATUS_CHOICES, default='draft')


	class Meta:
		ordering = ('-publish',) 


	def __str__(self):
		return self.tittle



	def get_absolute_url(self):
        
		a =  reverse('blog:post_detail',args=[
			self.publish.year,
			self.publish.strftime('%m'),
			self.publish.strftime('%d'),
			self.slug]
	
			)
		print a
		return a

class Comment(models.Model):
	"""docstring for coMM"""
	post = models.ForeignKey(Post
		,related_name='comments')
	name  = models.CharField(max_length=80)
	email =  models.EmailField()
	body  = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)


	class Meta(object):
	 	ordering = ('created',)

class Tag(models.Model):
	name = models.CharField(max_length=80)
	discription = models.CharField(max_length=160)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	posts = models.ManyToManyField(Post, through='TagPost')

class TagPost(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


	

		

     