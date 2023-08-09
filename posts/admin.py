from django.contrib import admin
from .models import Moviedata, Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Moviedata)