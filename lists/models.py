from django.db import models

class Item(models.Model):
	# map to table in db, id attr auto-generated,
	# but other columns need to be defined explicitly.
	text = models.TextField()