from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/<str:usrnm>/', Profile, name='Profile'),
    path('contact_us/<str:usrnm>/', Contact, name='Contact'),
    path('send_report/<str:usrnm>/', Report, name='Report')
 ]\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
