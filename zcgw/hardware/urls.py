from django.conf.urls import url,include
from hardware import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^city_id=(?P<city_id>\d+)/$',views.showcity,name='showcity'),
    url(r'^city_id=(?P<city_id>\d+)/type_id=(?P<type_id>\d+)$',views.showcity,name='showtype'),
]