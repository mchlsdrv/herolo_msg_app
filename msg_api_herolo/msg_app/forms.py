from django import forms
from tinymce.models import HTMLField
from datetime import datetime

# Create your models here.
class MessageForm(forms.Form):
	subject = forms.CharField(max_length=100)
	sender = forms.CharField(max_length=50)
	receiver = forms.CharField(max_length=50)
	# creation_date = forms.DateTimeField('creation date', default=datetime.now())
	content = HTMLField()

	class Meta:
		verbose_name_plural = 'Messages'

	def __str__(self):
		return self.subject

	def get_absolute_url(self):
		return reverse('msg_app:home')