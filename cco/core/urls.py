from django.conf.urls import url, include
from cco.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^contato/$', views.contato, name='contato'),
]
