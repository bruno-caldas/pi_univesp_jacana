from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from parceiros.views import carrega_parceiros
from . import views

app_name = 'parceiros'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', carrega_parceiros, name='parceiros'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)