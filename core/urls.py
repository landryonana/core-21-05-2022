from fileinput import filename
from re import template
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

from . import views

urlpatterns = [
    path('evangelisations-admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('', include("accounts.urls")),
    path('evangelisations/', include("evangelisations.urls")),
    path('rapports/', include("rapports.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
