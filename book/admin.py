from django.contrib import admin
from .models import Book, Review
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description','title')
admin.site.register(Book,BookAdmin)
admin.site.register(Review)
# Register your models here.
