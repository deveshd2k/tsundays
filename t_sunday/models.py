from django.db import models

# Create your models here.
class Players(models.Model):
	rank = models.IntegerField(default=0,blank=True)
	name = models.CharField(max_length=40)
	game1 = models.IntegerField(default=0,blank=True)
	game2 = models.IntegerField(default=0,blank=True)
	total = models.IntegerField(default=0,blank=True)

	def __str__(self):
		return self.name
