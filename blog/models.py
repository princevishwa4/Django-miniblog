from django.db import models


class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()