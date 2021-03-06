"""cco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^core/', include('cco.core.urls', namespace='core')),
    url(r'^dvrscan/', include('cco.dvrscan.urls', namespace='dvrscan')),
    url(r'^escala/', include('cco.escala.urls', namespace='escala')),
    url(r'^app/', include('cco.app.urls', namespace='app')),
    url(r'^sca/', include('cco.sca.urls', namespace='sca')),
    url(r'^chamado/', include('cco.chamado.urls', namespace='chamado')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^jet/', include('jet.urls', 'jet')),
    #url(r'^admin/', admin.site.urls),
]
