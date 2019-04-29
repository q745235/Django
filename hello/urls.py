from django.conf.urls import url
from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = 'hello'
urlpatterns = [
    # ex: /hello/
    url('', views.hello, {'a' : '123'}, name='hello'),
    url(r'^test/(?P<id>\d{2})/(?P<key>\w+)/$', views.test),
]