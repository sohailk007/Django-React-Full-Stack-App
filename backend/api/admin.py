from django.contrib import admin
from api.models import Note

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','created_at','author']