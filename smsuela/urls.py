from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace="home")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
