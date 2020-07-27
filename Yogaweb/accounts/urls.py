from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.user_login, name='user_login'), # its worked
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.signup, name='signup'),  # its worked

]
