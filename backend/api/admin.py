from django.contrib import admin
from api.models import Note, Account

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','created_at','author']
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display =  ["account_id", "introducer", "beneficiary", "created_by", "created_at"]
    
    


