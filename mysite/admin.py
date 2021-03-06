from django.contrib import admin
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Post, PostAdmin)
