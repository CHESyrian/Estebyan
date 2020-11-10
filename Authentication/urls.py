from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Register, Signing_Up, Login, Logging

urlpatterns = [
    path('register/', Register, name='Register'),
    path('signing_up/', Signing_Up, name='Signing_Up'),
    path('login/', Login, name="Login"),
    path('logging/', Logging, name='Logging')
] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
