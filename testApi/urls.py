from dj_rest_auth.registration.views import LoginView, RegisterView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view

from . import providers as socialProvider

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',
          include('dj_rest_auth.registration.urls')),

    path('dj-rest-auth/google/', socialProvider.GoogleLogin.as_view(),
          name='google_login'),
    path('dj-rest-auth/google/connect/',
          socialProvider.GoogleConnect.as_view(), name='google_connect'),


    path('post/', include('post.urls')),
    path('pay/', include('pay.urls')),

    path('todos/', include('todos.urls')),

    path('openapi/', get_schema_view(
        title="Mazyar",
        description="See API",
        version="1.0.0"), name='openapi-schema'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
