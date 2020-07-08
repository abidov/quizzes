from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('tests/', include('tests.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
