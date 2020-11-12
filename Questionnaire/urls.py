from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<str:usrnm>/add_questionnaire/', Add_Questionnaire, name='Add_Questionnaire'),
    path('<str:usrnm>/make_questionnaire/', Make_Questionnaire, name='Make_Questionnaire'),
    path('<str:usrnm>/search/<str:keyword>/', Search, name='Search')
] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
