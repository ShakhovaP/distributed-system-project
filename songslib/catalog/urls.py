from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^songs/$', views.SongListView.as_view(), name='songs'),
    path(r'^songs/(?P<pk>\d+)$', views.SongDetailView.as_view(), name='song-detail'),
    path(r'^singers/$', views.SingerListView.as_view(), name = 'singers'),
    path(r'^singers/(?P<pk>\d+)$', views.SingerDetailView.as_view(), name = 'singer-detail'),
]
