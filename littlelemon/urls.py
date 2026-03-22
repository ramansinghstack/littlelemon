
from django.contrib import admin
from django.urls import path
from django.urls import path, include  
from rest_framework import routers
from restaurant.views import MenuViewSet, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
# router.register(r'booking', BookingViewSet)
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
