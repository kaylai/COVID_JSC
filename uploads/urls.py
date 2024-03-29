from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^plotfile', views.plotfile, name='plotfile'),
    url(r'^maricopa', views.maricopa, name='maricopa'),
    url(r'^plotmaricopa', views.plotmaricopa, name='plotmaricopa'),
    url(r'^harris', views.harris, name='harris'),
    url(r'^salt_lake', views.salt_lake, name='salt_lake'),
    url(r'^plotsalt_lake', views.plotsalt_lake, name='plotsalt_lake'),
    url(r'^utah', views.utah, name='utah'),
    url(r'^plotutah', views.plotutah, name='plotutah'),
    url(r'^san_diego', views.san_diego, name='san_diego'),
    url(r'^plotsan_diego', views.plotsan_diego, name='plotsan_diego'),
    url(r'^clark', views.clark, name='clark'),
    url(r'^plotclark', views.plotclark, name='plotclark'),
    url(r'^travis', views.travis, name='travis'),
    url(r'^plottravis', views.plottravis, name='plottravis'),
    url(r'^westchester', views.westchester, name='westchester'),
    url(r'^plotwestchester', views.plotwestchester, name='plotwestchester'),
    url(r'^los_angeles', views.los_angeles, name='los_angeles'),
    url(r'^plotlos_angeles', views.plotlos_angeles, name='plotlos_angeles'),
    url(r'^miamidade', views.miamidade, name='miamidade'),
    url(r'^plotmiamidade', views.plotmiamidade, name='plotmiamidade'),
    url(r'^mclennan', views.mclennan, name='mclennan'),
    url(r'^plotmclennan', views.plotmclennan, name='plotmclennan'),
    url(r'^percapita', views.percapita, name='percapita'),
    url(r'^plotpercapita', views.plotpercapita, name='plotpercapita')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
