from rest_framework import routers
from .views import UsersViewSet, UserProfileViewSet, LoggedUserProfileViewSet, FieldInfoViewSet
from designation.views import DesignationViewSet
from program_app.views import ProgramViewSet
from project_app.views import ProjectViewSet, ProjectMemberViewSet
from profession_app.views import ProfessionViewSet
from certificate_app.views import CertificateViewSet
from department_app.views import DepartmentViewSet
from organization_address_app.views import OrganizationProfileViewSet, ContractViewSet, RatingViewSet, InvitationsViewSet, NotificationsViewSet, NotificationViewsViewSet
from field_supervisor_app.views import FieldSupervisorProfileViewSet
from student_profile_app.views import StudentProfileViewSet, StudentsProfessionsViewSet, FieldReportViewSet
from alumni_profile_app.views import AlumniProfileViewSet, AlumniProfessionViewSet
from staff_profile_app.views import StaffProfileViewSet
from field_post_app.views import FieldPostViewSet, FieldApplicationViewSet, FieldPostProfessionViewSet, FieldPostProgramViewSet
from internship_post_app.views import (InternshipPostViewSet, InternshipApplicationViewSet,
 InternshipApplicationStatusViewSet, ApplicantLevelViewSet, InterviewScheduleViewSet)
from announcement_app.views import AnnouncementViewSet
from questions_app.views import (QuestionsViewSet, MultipleChoicesViewSet,
ApplicantAnswerViewSet, )
from cv_app.views import (PersonalInformationViewSet, EducationInformationViewSet,
ExperienceInformationViewSet)

router = routers.DefaultRouter()

router.register('field_info', FieldInfoViewSet, 'field_info')
router.register('cvs_experience_informations', ExperienceInformationViewSet, 'cvs_experience_informations')
router.register('cvs_personal_informations', PersonalInformationViewSet, 'cvs_personal_informations')
router.register('cvs_education_informations', EducationInformationViewSet, 'cvs_education_informations')
router.register('questions', QuestionsViewSet, 'questions')
router.register('multiplechoices', MultipleChoicesViewSet, 'multiplechoices')
router.register('user_profile', LoggedUserProfileViewSet, 'user_profile')
router.register('announcements', AnnouncementViewSet, 'announcements')
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
router.register('contracts', ContractViewSet, 'contracts')
router.register('alumni_professions', AlumniProfessionViewSet, 'alumni_professions')
router.register('alumni_ratings', RatingViewSet, 'alumni_ratings')
router.register('staffs_profiles', StaffProfileViewSet, 'staffs_profiles')
router.register('field_posts', FieldPostViewSet, 'field_posts')
router.register('field_post_professions', FieldPostProfessionViewSet, 'field_post_professions')
router.register('field_post_programs', FieldPostProgramViewSet, 'field_post_programs')
router.register('field_applications', FieldApplicationViewSet, 'field_applications')
router.register('internship_posts', InternshipPostViewSet, 'internship_posts')
router.register('interview_schedules', InterviewScheduleViewSet, 'interview_schedules')
router.register('internship_applications', InternshipApplicationViewSet, 'internship_applications')
router.register('notifications', NotificationsViewSet, 'notifications')
router.register('notifications_views', NotificationViewsViewSet, 'notifications_views')
router.register('internship_applications_status', InternshipApplicationStatusViewSet, 'internship_applications_status')
router.register('applicant_levels', ApplicantLevelViewSet, 'applicant_levels')
router.register('job_invitations', InvitationsViewSet, 'alumni_invitation')


urlpatterns = router.urls
