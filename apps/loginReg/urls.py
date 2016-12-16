from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^dashboard$', views.dashboard, name = 'dashboard'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^addBook$', views.addBook, name = 'addBook'),
    url(r'^delete/(?P<author_id>\d*)$', views.delete),
    url(r'^wish_items/(?P<author_id>\d*)$', views.wish_items),
]
