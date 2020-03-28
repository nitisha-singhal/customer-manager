from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='base'),
    path('clist/', views.clist, name='clist'),
    path('rtask/', views.rtask, name='rtask'),
    path('atask/', views.atask, name='atask'),
    path('user/',views.user, name='user'),
    path('items/',views.items, name='items'),
    path('profile/',views.profile, name='profile'),
    path('department/',views.department, name='department'),
]
