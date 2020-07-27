from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post_Blog, Video_list, Image_list

admin.site.register(Post_Blog)
admin.site.register(Video_list)
admin.site.register(Image_list)

admin.site.unregister(Group)
admin.site.site_header = 'Admin-master Dashboard'
admin.site.site_title = 'Welcome to the Yoga Dashboard'
admin.site.index_title = 'Welcome to the This Yoga Portal'
