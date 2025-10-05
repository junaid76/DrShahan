from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from portfolio import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('gallery/', v.gallery, name='gallery'),
    path('pair/<int:pair_id>/', v.pair_detail, name='pair_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)