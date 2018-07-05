from django.conf.urls import include, url
from firstapp import views
#from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'firstapp.views.index', name='index'),
     
     # r means ragular expression
     # ^ means begin with
    # url(r'^blog/', include('blog.urls')),

    #    url(r'^admin/', include(admin.site.urls)),
]
