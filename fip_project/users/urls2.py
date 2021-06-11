from rest_framework import routers
from .api2 import ( StudentProfessionViewSet, 
    ProgramsByDepartmentViewSet, StudentsByProgramViewSet, 
    StudentsByDepartmentViewSet, StudentsByAcademicSpervisorViewSet,
    StudentsByStatusViewSet, StudentsByFieldSpervisorViewSet,
    StudentsByYearOfStudyViewSet, AlumniProfessionViewSet,
    AlumniByOrganizationViewSet, StudentsByOrganizationViewSet,
    AlumniByCompletionYearViewSet, AlumniByDegreeProgramViewSet,
    AlumniByDepartmentViewSet, FieldPostByOrganizationViewSet,
    FieldApplicationByPostViewSet, FieldPostProfessionViewSet,
    FieldApplicationByStudentViewSet, InternshipPostByOrganizationViewSet,
    InternshipApplicationByPostViewSet,
    InternshipApplicationByAlumniViewSet, StudentReportViewSet,
    AlumniByStatusViewSet, SingleUserProfileViewSet,
    SingleAlumniProfileViewSet, AnnouncementsByDesignationsViewSet,
    ProjectsByMemberViewSet, ProjectMembersViewSet,
    QuestionChoicesViewSet, ApplicantMarksViewSet,
    ApplicantAnswersViewSet, QuestionsByProfessionsViewSet,
    InternshipApplicationByOrganizationViewSet,
    InterviewScheduleByPostViewSet, OrganizationContractsViewSet,
    SingleOrganizationProfileViewSet, CvPersonalInformationViewSet,
    CvEducationInformationViewSet, CvExperienceInformationViewSet,
    AlumniCertificatesViewSet, PubllishedAlumniViewSet,
    AlumniInvitationsViewSet, OrganizationInvitationsViewSet,
    SingleStaffProfileViewSet
    )

router = routers.DefaultRouter()

router.register('published_alumni', PubllishedAlumniViewSet, 'published_alumni')
router.register(r'alumni/(?P<alumniId>\d+)/certificates', AlumniCertificatesViewSet, 'alumni-certificates')
router.register(r'alumni/(?P<alumniId>\d+)/cv_experience_informations', CvExperienceInformationViewSet, 'alumni-cv-experience-informations')
router.register(r'alumni/(?P<alumniId>\d+)/cv_personal_informations', CvPersonalInformationViewSet, 'alumni-cv-personal-informations')
router.register(r'alumni/(?P<alumniId>\d+)/cv_education_informations', CvEducationInformationViewSet, 'alumni-cv-education-informations')
router.register(r'post/(?P<postId>\d+)/schedule', InterviewScheduleByPostViewSet, 'post-schedule')
router.register(r'profession/(?P<professionId>\d+)/questions', QuestionsByProfessionsViewSet, 'profession_questions')
router.register(r'alumni/(?P<alumniId>\d+)/post/(?P<postId>\d+)/marks', ApplicantMarksViewSet, 'alumni-marks')
router.register(r'alumni/(?P<alumniId>\d+)/post/(?P<postId>\d+)/answers', ApplicantAnswersViewSet, 'alumni-answers')
router.register(r'question/(?P<questionId>\d+)/choices', QuestionChoicesViewSet, 'question-choices')
router.register(r'user/(?P<userId>\d+)/profile', SingleUserProfileViewSet, 'user-profile')
router.register(r'member/(?P<memberId>\d+)/projects', ProjectsByMemberViewSet, 'user-projects')
router.register(r'project/(?P<projectId>\d+)/members', ProjectMembersViewSet, 'project-members')
router.register(r'designation/(?P<designationId>\d+)/announcements', AnnouncementsByDesignationsViewSet, 'users-announcements')
router.register(r'student/(?P<studentId>\d+)/professions', StudentProfessionViewSet, 'student-professions')
router.register(r'student/(?P<studentId>\d+)/report', StudentReportViewSet, 'student-report')
router.register(r'alumni/(?P<alumniId>\d+)/professions', AlumniProfessionViewSet, 'alumni-professions')
router.register(r'alumni/(?P<alumniId>\d+)/profile', SingleAlumniProfileViewSet, 'alumni-profile')
router.register(r'staff/(?P<staffId>\d+)/profile', SingleStaffProfileViewSet, 'staff-profile')
router.register(r'field_post/(?P<postId>\d+)/professions', FieldPostProfessionViewSet, 'field_post-professions')
router.register(r'department/(?P<departmentId>\d+)/programs', ProgramsByDepartmentViewSet, 'department-programs')
router.register(r'alumni_by_department/(?P<departmentId>\d+)', AlumniByDepartmentViewSet, 'alumni_by_department')
router.register(r'organization/(?P<organizationId>\d+)/students', StudentsByOrganizationViewSet, 'organization-students')
router.register(r'organization/(?P<organizationId>\d+)/applications', InternshipApplicationByOrganizationViewSet, 'organization-internship-applications')
router.register(r'organization/(?P<organizationId>\d+)/field_posts', FieldPostByOrganizationViewSet, 'organization-field-posts')
router.register(r'organization/(?P<organizationId>\d+)/internship_posts', InternshipPostByOrganizationViewSet, 'organization-internship-posts')
router.register(r'organization/(?P<organizationId>\d+)/contracts', OrganizationContractsViewSet, 'organization-contracts')
router.register(r'organization/(?P<organizationId>\d+)/profile', SingleOrganizationProfileViewSet, 'single-organization-profile')
router.register(r'alumni_by_organization/(?P<organizationId>\d+)', AlumniByOrganizationViewSet, 'alumni_by_organization')
router.register(r'program/(?P<programId>\d+)/students', StudentsByProgramViewSet, 'program-students')
router.register(r'alumni_by_degree_program/(?P<programId>\d+)', AlumniByDegreeProgramViewSet, 'alumni_by_degree_program')
router.register(r'department/(?P<departmentId>\d+)/students', StudentsByDepartmentViewSet, 'department-students')
router.register(r'academic_supervisor/(?P<supervisorId>\d+)/students', StudentsByAcademicSpervisorViewSet, 'academic-supervisor-students')
router.register(r'field_supervisor/(?P<supervisorId>\d+)/students', StudentsByFieldSpervisorViewSet, 'field-supervisor-students')
router.register(r'students_by_status/(?P<status>\w+)', StudentsByStatusViewSet, 'students-by-status')
router.register(r'alumni_by_status/(?P<status>\w+)', AlumniByStatusViewSet, 'alumni-by-status')
router.register(r'students_by_year_of_study/(?P<year>\d+)', StudentsByYearOfStudyViewSet, 'students-by-year-of-study')
router.register(r'alumni_by_completion_year/(?P<year>\d+)', AlumniByCompletionYearViewSet, 'alumni_by_completion_year')
router.register(r'field_post/(?P<postId>\d+)/applications', FieldApplicationByPostViewSet, 'field-applications-by-post')
router.register(r'internship_post/(?P<postId>\d+)/applications', InternshipApplicationByPostViewSet, 'internship-applications-by-post')
router.register(r'student/(?P<studentId>\d+)/field_applications', FieldApplicationByStudentViewSet, 'field-applications-by-student')
router.register(r'alumni/(?P<alumniId>\d+)/internship_applications', InternshipApplicationByAlumniViewSet, 'internship-applications-by-alumni')
router.register(r'alumni/(?P<alumniId>\d+)/invitations', AlumniInvitationsViewSet, 'alumni_invitations')
router.register(r'organization/(?P<organizationId>\d+)/invitations', OrganizationInvitationsViewSet, 'organization_invitations')




urlpatterns = router.urls
