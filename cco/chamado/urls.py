from django.conf.urls import url, include
from cco.chamado import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
