from django.contrib import admin

# Register your models here.
from .models import Artist, Tag


admin.site.register(Artist)
admin.site.register(Tag)