from django.conf.urls import url, include
from django.contrib import admin
from scrap import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("scrap.urls")),
   
    
    url(r'^datatable/$', views.datatable, name="datatable"),
    url(r'^table_api/$', views.table_api, name="table_api"),
    
    url(r'^savedata/$', views.savedata, name="savedata"),
    
    url(r'^(?P<u_id>\d{0,50})/$', views.chart, name="chart"),
    url(r'^json/(?P<u_id>\d{0,50})/$', views.json_page, name="json"),
    
    
    
]

