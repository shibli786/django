from django.contrib import admin

from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('tittle','slug','author','publish','status')
	list_filter = ('status', 'created', 'publish','author')
	search_fields= ('title','body')
	prepopulated_fields ={'slug':('tittle',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status','publish']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','body','post','created','active')
	list_filter = ('active','created','updated' )
	search_fields = ('name','email','body')

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)