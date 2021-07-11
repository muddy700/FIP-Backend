from django.contrib import admin
from users.views import RegisterAPI, LoginAPI, UserAPI, ChangePasswordView
from knox import views as knox_views
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
openapi.Info(
title="FIPMS API",
default_version='v1',
description="Test description",
terms_of_service="#",
contact=openapi.Contact(email="mohamedmfaume700@gmail.com"),
license=openapi.License(name="TEST License"),
),
public=True,
# permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('users.urls')),
    path('api/', include('users.urls')),
    path('api/filter/', include('users.urls2')),
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/auth/user', UserAPI.as_view()),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change_password/', ChangePasswordView.as_view(), name='change-password'),

    # path('swagger(?P<format>.json|.yaml)$’, schema_view.without_ui(cache_timeout=0), name=’schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

admin.site.site_header = 'FIPMS Admin Panel'
admin.site.site_title = 'Admin'