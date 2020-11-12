from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', Register, name='Register'),
    path('signing_up/', Signing_Up, name='Signing_Up'),
    path('login/', Login, name="Login"),
    path('logging/', Logging, name='Logging'),
    path('username_validate/<str:usrnm>/', Username_Validate, name='Username_Validate')
] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
