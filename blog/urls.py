from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url(r'^$', views.PostsView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PostsDetailView.as_view()),

]