from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='hello'),
    # url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
    url(r'^numbers/$', views.NumberList.as_view(), name="number_list"),
    url(r'^numbers/new/', views.new_number, name="new")
]
