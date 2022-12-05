from django.contrib import admin
from django.urls import path
from core.views import car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', car)
]