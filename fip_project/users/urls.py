from rest_framework import routers
from .views import UsersViewSet, UserProfileViewSet
from designation.views import DesignationViewSet
from program_app.views import ProgramViewSet
from project_app.views import ProjectViewSet, ProjectMemberViewSet
from profession_app.views import ProfessionViewSet
from certificate_app.views import CertificateViewSet
from department_app.views import DepartmentViewSet
from organization_address_app.views import OrganizationProfileViewSet
from field_supervisor_app.views import FieldSupervisorProfileViewSet
from student_profile_app.views import StudentProfileViewSet, StudentsProfessionsViewSet, FieldReportViewSet
from alumni_profile_app.views import AlumniProfileViewSet, AlumniProfessionViewSet
from staff_profile_app.views import StaffProfileViewSet
from field_post_app.views import FieldPostViewSet, FieldApplicationViewSet, FieldPostProfessionViewSet
from internship_post_app.views import InternshipPostViewSet, InternshipPostProfessionViewSet, InternshipApplicationViewSet

router = routers.DefaultRouter()

router.register('users', UsersViewSet, 'users')
router.register('users_profiles', UserProfileViewSet, 'users_profiles')
router.register('designations', DesignationViewSet, 'designations')
router.register('departments', DepartmentViewSet, 'departments')
router.register('programs', ProgramViewSet, 'programs')
router.register('projects', ProjectViewSet, 'projects')
router.register('projects_members', ProjectMemberViewSet, 'projects_members')
router.register('certificates', CertificateViewSet, 'certificates')
router.register('professions', ProfessionViewSet, 'professions')
router.register('organization_profile', OrganizationProfileViewSet, 'organization_profile')
router.register('field_supervisors_profiles', FieldSupervisorProfileViewSet, 'field_supervisors_profiles')
router.register('students_profiles', StudentProfileViewSet, 'students_profiles')
router.register('field_reports', FieldReportViewSet, 'field_reports')
router.register('students_professions', StudentsProfessionsViewSet, 'students_professions')
router.register('alumni_profiles', AlumniProfileViewSet, 'alumni_profiles')
router.register('alumni_professions', AlumniProfessionViewSet, 'alumni_professions')
router.register('staffs_profiles', StaffProfileViewSet, 'staffs_profiles')
router.register('field_posts', FieldPostViewSet, 'field_posts')
router.register('field_post_professions', FieldPostProfessionViewSet, 'field_post_professions')
router.register('field_applications', FieldApplicationViewSet, 'field_applications')
router.register('internship_posts', InternshipPostViewSet, 'internship_posts')
router.register('internship_applications', InternshipApplicationViewSet, 'internship_applications')
router.register('internship_post_professions', InternshipPostProfessionViewSet, 'internship_post_professions')


urlpatterns = router.urls
