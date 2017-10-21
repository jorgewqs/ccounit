from django.conf.urls import url, include
from cco.escala import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
