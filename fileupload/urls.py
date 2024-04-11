from django.urls import path
from .views import home,upload, login_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    #path('',home),
    path('uploadfile/', upload, name='upload'),
    path('',login_view, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
