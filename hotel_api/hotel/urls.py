from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # hotel/add
   url(r'^add/$', views.HotelCreate.as_view(success_url="/hotel/"), name='hotel-add')
]