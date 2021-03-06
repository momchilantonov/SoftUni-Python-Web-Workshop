from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("petstagram.common.urls")),
    path("pets/", include('petstagram.pets.urls')),
    path('account/', include('petstagram.account.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
