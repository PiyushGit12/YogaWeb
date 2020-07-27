from . import views
from django.urls import path

urlpatterns = [

    path('', views.user_blog_ui, name='user_blog_ui'),  # User HOME-PAGE-UI
    path('Blog-List/', views.blog_post_ui, name='blog_post_ui'),  # its  worked
    path('Blog-post/upload/', views.blog_post_upload, name='blog_post_upload'),  # its  worked
    path('Images/', views.img_list, name='img_list'),  # its worked
    path('Videos/', views.vid_list, name='vid_list'),  # its  worked
    path('Images/upload/', views.upload_img, name='upload_img'),  # its worked
    path('Video/upload/', views.upload_video, name='upload_video'),  # its  worked
    path('delete-blog/<int:id>/', views.delete_blog, name='delete_blog'),  # its  not  work
    path('update-blog/<int:id>/', views.update_blog, name='update_blog'),  # its  worked

]
