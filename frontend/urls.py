from django.contrib import admin
from django.urls import path, include
from frontend import views, helper

urlpatterns = [
    path('',views.index, name="home"),
    path('fbapp',views.index, name="home_fb"),
    path('twitter/',views.login_twitter, name='twitter'),
    path('user_detail/',helper.user_detail, name='user_detail'),
    path('user_detail_withoutid/',helper.get_user_dtl, name='user_det'),
    path('non_public/',helper.get_user_dtl, name='user_det')
]
