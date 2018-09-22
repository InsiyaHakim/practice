from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index , name="index"),
    url(r'^create$', views.create , name="create"),
    url(r'^login$', views.login , name="log"),
]