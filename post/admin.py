from django.contrib import admin
import post.models

admin.site.register(post.models.Post)
admin.site.register(post.models.Tag)
