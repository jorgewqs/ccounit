from django.conf.urls import url, include
from cco.dvrscan import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
