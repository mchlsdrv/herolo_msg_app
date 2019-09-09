from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Message(models.Model):
	subject = models.CharField(max_length=100)
	sender = models.CharField(max_length=50)
	receiver = models.CharField(max_length=50)
	creation_date = models.DateTimeField('creation date', default=datetime.now())
	content = models.TextField()
	read = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = 'Messages'

	def __str__(self):
		return self.subject

	def get_absolute_url(self):
		return reverse('msg_app:home')