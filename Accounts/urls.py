from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/<str:usrnm>/', Profile, name='Profile'),
 ]\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
