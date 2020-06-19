from django.urls import path
from . import views

app_name='app'

urlpatterns = [
    path('',views.signup,name='signup'),
    path('user_login/',views.user_login, name = "login"),
    path('user_logout/',views.user_logout,name = "logout"),
    path('home/<int:pk>/',views.home,name = "home"),
    path('post/<int:pk>/',views.makepost,name="post"),
    path('likepost/',views.likepost,name="likepost"),
    path('comments/',views.commentspost,name="comments"),
    path('profile/<int:mypk>/<int:ppk>/' , views.profile , name="profile"),
    path('cover_pic_change/<int:pk>/',views.cover_pic_change ,name="cover_pic_change"),
    path('profile_pic_change/<int:pk>/',views.profile_pic_change ,name="profile_pic_change"),
    path('addbio/<int:pk>/',views.addbio,name="addbio"),
]
