from django.contrib import admin
from django.urls import path, include
from .views import view_bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view_bienvenidos, name="Bienvenidos"),
    path("crud/", include('TecHard.crud.urls')),
]