from django.contrib import admin
from .models import PostModel,Comment

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','author','content','date_created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','parent')
    
admin.site.register(PostModel,PostModelAdmin)
admin.site.register(Comment,CommentAdmin)