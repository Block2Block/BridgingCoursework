from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^[0-9]+', views.post_full, name='post_full'),
    url(r'^', views.post_list, name='post_list'),
]
