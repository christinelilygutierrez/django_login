from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^validate/$', views.loginValidate, name='loginValidate'),
    url(r'^account/$', views.account, name='account'),
    url(r'^test/$', views.permission_test, name='test'),
]
