# urls.py
from django.urls import path
from .views import video_list, audio_list, index,about,service,login,reg,dashboard,dash,cont

urlpatterns = [
    path('videos/', video_list, name='video_list'),
    path('audios/', audio_list, name='audio_list'),
    path('',index,name='ind'),
    path('about/',about),
    path('service/',service),
    path('login/',login),
    path('reg/',reg),
    path('udash/',dashboard),
    path('dash/',dash,name='dash'),
    path('cont/',cont)

]
