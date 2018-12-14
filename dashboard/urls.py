# from django.contrib import admin
from django.urls import include, path
from . import views


from django.conf.urls import url, include
from rest_framework import routers
from . import apiview

router = routers.DefaultRouter()
router.register(r'backups', apiview.BackupViewSet)
router.register(r'hosts', apiview.HostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index),
    path('api/status', views.status),
    path('api/status/<int:id>', views.details),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


#
# urlpatterns = [
#     path('', views.index),
#     path('api/status', views.status),
#     path('api/status/<int:id>', views.details),
# ]
