from django.contrib import admin
from django.urls import path, include
from landing.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Главная страница
    path('contact/', include('landing.urls')),  # Форма обратной связи
]

# Добавляем поддержку медиафайлов
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
