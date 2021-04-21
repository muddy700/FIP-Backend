from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('designations', views.DesignationViewSet, 'designations')

urlpatterns = router.urls