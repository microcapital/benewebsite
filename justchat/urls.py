from django.conf.urls import include, url
from django.contrib import admin
from accounts import views

urlpatterns = [
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^$', views.index, name='index'),
]
