from django.conf.urls import url
from django.utils.http import urlsafe_base64_decode

from . import views
app_name= 'emp'
urlpatterns = [
    url(r'^$',views.showform,name='index'),
    url(r'^home/$', views.home, name="home"),
    url(r'^table',views.showTable,name='table'),
    url(r'^upload',views.uploadCSV,name='upload'),
    url(r'^download/CSV_file',views.downloadCSV,name='downloadcsv'),
    url(r'^download/',views.download,name='download'),
    url(r'^search/$',views.searchEmployee,name='search'),
    url(r'^searchdata/',views.empsearch, name="searchdata"),
    url(r'^(?P<item_id>[a-zA-Z0-9]+)/delete/$', views.objectDelete, name='delete_object'),
    url(r'^(?P<item_id>[a-zA-Z0-9]+)/update/$', views.objectUpdate, name='update_object'),
    url(r'^updatedata/',views.update,name="updatedata"),

]