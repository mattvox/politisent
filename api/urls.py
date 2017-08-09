from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TweetsView.as_view(), name='tweets'),
]
