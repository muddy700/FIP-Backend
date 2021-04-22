from rest_framework import routers
from .views import UsersViewSet
from designation.views import DesignationViewSet
from program_app.views import ProgramViewSet
from project_app.views import ProjectViewSet
from profession_app.views import ProfessionViewSet
from organization_app.views import OrganizationViewSet
from certificate_app.views import CertificateViewSet
from department_app.views import DepartmentViewSet
from organization_address_app.views import OrganizationAddressViewSet
from field_supervisor_app.views import FieldSupervisorProfileViewSet
from student_profile_app.views import StudentProfileViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet, 'users')
router.register('designations', DesignationViewSet, 'designations')
router.register('departments', DepartmentViewSet, 'departments')
router.register('programs', ProgramViewSet, 'programs')
router.register('projects', ProjectViewSet, 'projects')
router.register('certificates', CertificateViewSet, 'certificates')
router.register('professions', ProfessionViewSet, 'professions')
router.register('organizations', OrganizationViewSet, 'organizations')
router.register('organization_address', OrganizationAddressViewSet, 'organization_address')
router.register('field_supervisors_profiles', FieldSupervisorProfileViewSet, 'field_supervisors_profiles')
router.register('students_profiles', StudentProfileViewSet, 'students_profiles')

urlpatterns = router.urls
