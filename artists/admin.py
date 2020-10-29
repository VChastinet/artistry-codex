from django.contrib import admin

# Register your models here.
from .models import Artist, State, Tag

class ArtistAdmin(admin.ModelAdmin):
  fieldsets = [('something', {'fields': ['name']}),]

admin.site.register(Artist)
admin.site.register(State)
admin.site.register(Tag)