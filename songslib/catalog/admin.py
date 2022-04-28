from django.contrib import admin

# Register your models here.
from .models import Singer, Genre, Song

admin.site.register(Genre)

class SongInline(admin.TabularInline):
    model = Song
    extra = 0

# Define the admin class
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [SongInline]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'singer', 'display_genre')

    fieldsets = (
        (None, {
            'fields': ('name','singer', 'genre')
        }),
        ('Details', {
            'fields': ('lyrics', 'chords')
        }),
    )