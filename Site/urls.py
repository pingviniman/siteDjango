from django.conf.urls import url, include
from rest_framework import routers
from Site import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'persons', views.PersonViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^index/(?P<pk>[0-9]+)/?$', views.PersonDetailView.as_view(),name='person_detail'),
    url(r'^index/$',views.PersonView.as_view()),

]