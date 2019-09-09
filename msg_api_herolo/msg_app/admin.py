from django.contrib import admin
from .models import Message
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class MsgAdmin(admin.ModelAdmin):
	fieldsets = [
	('Basic Information', {'fields': ['subject', 'creation_date']}),
	('Users', {'fields': ['sender', 'receiver']}),
	('Content', {'fields': ['content']})			
	]
	formfield_overrides = {
							models.TextField: {'widget': TinyMCE()}
						  }

admin.site.register(Message, MsgAdmin)
