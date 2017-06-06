from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^aboutus', views.about, name='about'),
    url(r'^contactus', views.contact, name='contact'),
    url(r'^appointments', views.appoint, name='appointments'),

]