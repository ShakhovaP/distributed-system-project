from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^songs/$', views.SongListView.as_view(), name='songs'),
    re_path(r'^songs/(?P<pk>\d+)$', views.SongDetailView.as_view(), name='song-detail'),
    re_path(r'^singers/$', views.SingerListView.as_view(), name = 'singers'),
    re_path(r'^singers/(?P<pk>\d+)$', views.SingerDetailView.as_view(), name = 'singer-detail'),
]
