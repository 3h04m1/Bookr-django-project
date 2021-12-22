"""bookr URL Configuration

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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings
from .views import profile, reading_history
# from debug_toolbar import urls as debug_urls
import debug_toolbar


urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'),
                              namespace='accounts')),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/reading_history', reading_history, name='reading_history'),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('filter_demo/', include('filter_demo.urls')),
    path('book_management/', include('book_management_app.urls')),
    path('test/', include('bookr_test.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),

]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
