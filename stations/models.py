from django.db import models
from django.contrib import admin


class Station(models.Model):
	name 			= models.CharField(('name'), max_length=255)
	lat 			= models.CharField(('lat'), max_length=255)
	lng 			= models.CharField(('lng'), max_length=255)
	school			= models.CharField(('school'), max_length=255)
	state			= models.CharField(('state'), max_length=255)
	url 			= models.CharField(('url'), max_length=255)


	#class Meta:
	#	ordering = ('-created')

	def __unicode__(self):
		return self.name