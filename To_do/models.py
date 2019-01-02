from django.db import models


class ToDo(models.Model):

	text = models.CharField(max_length=200, blank=True)
	done = models.BooleanField()
