from django.conf.urls import url,include
from hardware import views
urlpatterns = [
    url(r'^index/', views.index),
]