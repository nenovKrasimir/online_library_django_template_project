from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import online_library_django_template_project.common_app.urls
import online_library_django_template_project.library_app.urls
import online_library_django_template_project.profile_app.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(online_library_django_template_project.common_app.urls)),
    path('', include(online_library_django_template_project.library_app.urls)),
    path('profile/', include(online_library_django_template_project.profile_app.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
