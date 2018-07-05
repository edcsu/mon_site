from django.conf.urls import include, url
from django.contrib import admin
#from . import urls from this folder
from firstapp import urls # import from the app folder

urlpatterns = [
    # Examples:
    # url(r'^$', 'sewasite.views.home', name='home'),
    # if the url isnot admin, url is in this file, use appp name
    url(r'', include('firstapp.urls')), 

    url(r'^admin/', include(admin.site.urls)),
]
