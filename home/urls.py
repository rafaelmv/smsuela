from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # url(r'^login/$', views.auth_login, name='authentication'),
    # url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='hello'),
    # url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
    url(r'^numbers/$', views.NumberList.as_view(), name="number_list"),
    url(r'^number/new/', views.new_number, name="new")
]
