from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from portal.views import page_not_found_view, page_not_found_view2

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("main.urls")),
    path("phonebook/", include("phonebook.urls")),
    path("accounts/", include("accounts.urls")),
)

handler404 = page_not_found_view  # type: ignore
handler403 = page_not_found_view2

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
