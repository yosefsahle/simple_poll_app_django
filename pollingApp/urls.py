
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('pools.urls')),
    path('api/',include('pools.api_urls')),
]
