from django.conf.urls import include, url

from api.views import (ManufacturerViewSet,
                       ShoeViewSet,
                       ShoeColorViewSet,
                       ShoeTypeViewSet,
                       UserViewSet
)

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'shoe', ShoeViewSet, basename='shoe')
router.register(r'shoecolor', ShoeColorViewSet)
router.register(r'shoetype', ShoeTypeViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))

]