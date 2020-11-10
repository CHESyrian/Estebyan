from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Add_Questionnaire, Make_Questionnaire

urlpatterns = [
    path('add_questionnaire/', Add_Questionnaire, name='Add_Questionnaire'),
    path('make_questionnaire/', Make_Questionnaire, name='Make_Questionnaire')
] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
