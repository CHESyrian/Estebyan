from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *


urlpatterns = [
    path('contact_us/', Contact, name='Contact'),
    path('send_report/', Report, name='Report'),
]\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
