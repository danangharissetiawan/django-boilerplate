"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler403
from django.contrib import admin
from django.urls import path, include
from manage import get_env_variable
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from main import views
# from django.conf.urls import handler404, handler500


urlpatterns = [
    path('<filename>', views.home_files, name='home-files'),
    
]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
)

handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500


DJANGO_SETTINGS_MODULE = get_env_variable('DJANGO_SETTINGS_MODULE')
# if DJANGO_SETTINGS_MODULE == 'config.settings.development':
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
# elif settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

