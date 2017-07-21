from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^aboutus', views.about, name='about'),
    url(r'^contactus', views.contact, name='contact'),
    url(r'^appointments', views.appoint, name='appointments'),
    url(r'^services/(?P<id>[0-9]+)/$', views.service_detailed, name='sDetail'),
    url(r'^products/(?P<id>[0-9]+)/$', views.product_detailed, name='pDetail'),
]
