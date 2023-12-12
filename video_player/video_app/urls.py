from django.urls import path
from video_app.views import *

urlpatterns = [
    path('', ARVideoPlayer.home_view, name='index'),
    path('about-us/', ARVideoPlayer.about_view, name='about-us'),
    path('contact-us', ARVideoPlayer.contact_view, name='contact-us'),

    path('search/', ARVideoPlayer.search, name='search'),

    path('videos/<slug:category_slug>/', ARVideoPlayer.show_video, name='videos'),
    path('videos/<slug:category_slug>/<slug:product_slug>/', ARVideoPlayer.show_single_video, name='single-video'),

    # USER AUTH #
    path('login/', UserAuth.user_login, name='user-login'),
    path('register/', UserAuth.user_register, name='user-register'),
    path('logout/', UserAuth.user_logout, name='user-logout'),

]