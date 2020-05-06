from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title = models.CharField('TITLE', max_length=50)
	slug = models.SlugField('SLUG', max_length=50, help_text = 'one word for title alias', allow_unicode=True)
	description = models.CharField('DESCRIPTION', max_length=100, help_text = 'simple description')
	content = models.TextField('CONTENT')
	create_dt = models.DateTimeField('CREATE DATE', auto_now_add = True)
	modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)
	tags = TaggableManager(blank=True)

	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'blog_posts'
		ordering = ('-modify_dt',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=(self.slug,))

	def get_next(self):
		return self.get_next_by_modify_dt()

	def get_previous(self):
		return self.get_previous_by_modify_dt()

	@property
	def like_count(self):
		return self.like_set.count()

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
	content = models.CharField('COMMENT', max_length=200)
	create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True, null=True)
	modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True, null=True)

	class Meta:
		ordering = ['-create_dt']

	def __str__(self):
		return self.content

class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True, null=True)
	
	class Meta:
	    unique_together = (("post", "user"),)
	    ordering = ['-create_dt']