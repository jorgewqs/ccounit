from django.conf.urls import url, include
from cco.sca import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
