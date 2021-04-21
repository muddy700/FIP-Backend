from .api import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UsersViewSet, 'users')

urlpatterns = router.urls