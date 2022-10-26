from django.contrib import admin
from django.urls import path, include
from api.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include(router.urls)),
]
