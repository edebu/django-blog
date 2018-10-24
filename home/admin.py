from django.contrib import admin
from .models import AddLink


class AddLinkAdmin(models.ModelAdmin):
	list_display = ['link']
	admin.site.register(AddLink, AddLinkAdmin)