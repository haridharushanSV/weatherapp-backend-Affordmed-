from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .import views

router=routers.DefaultRouter()
router.register(r'data',views.dataViewSet,'data')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/',include(router.urls)), 
]