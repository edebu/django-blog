from django.db import models

class AddLink(models.Model):
	link = models.CharField(max_length=200)
	