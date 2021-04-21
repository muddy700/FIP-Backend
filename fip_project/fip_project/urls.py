from django.contrib import admin
from users.views import RegisterAPI, LoginAPI, UserAPI, UsersViewSet
from knox import views as knox_views
from django.urls import path, include

urlpatterns = [
    path('api/', include('designation.urls')),
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/auth/user', UserAPI.as_view()),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]