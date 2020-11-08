from django.contrib import admin
from .models import Post,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title','body']

admin.site.register(Post,PostAdmin)

admin.site.register(Category)