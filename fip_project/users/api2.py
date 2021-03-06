from rest_framework import permissions
from rest_framework import viewsets, mixins

from staff_profile_app.models import StaffProfile
from staff_profile_app.serializers import StaffProfileSerializer
from student_profile_app.serializers import StudentProfessionSerializer, StudentProfileSerializer, FieldReportSerializer
from alumni_profile_app.serializers import AlumniProfileSerializer, AlumniProfessionSerializer, PublishedAlumniSerializer
from student_profile_app.models import StudentProfession, StudentProfile, FieldReport
from alumni_profile_app.models import AlumniProfile, AlumniProfession
from program_app.serializers import ProgramSerializer
from program_app.models import Program
from field_post_app.models import FieldApplication, FieldPost, FieldPostProfession, FieldPostProgram
from field_post_app.serializers import FieldPostProfessionSerializer, FieldApplicationSerializer, FieldPostSerializer, FieldPostProgramSerializer
from internship_post_app.models import InternshipApplication, InternshipPost, InterviewSchedule
from internship_post_app.serializers import InternshipPostSerializer, InternshipApplicationSerializer, InterviewScheduleSerializer
from .models import UserProfile
from .serializers import UserProfileSerializer
from announcement_app.models import Announcement
from announcement_app.serializers import AnnouncementSerializer
from project_app.models import ProjectMember
from project_app.serializers import ProjectMemberSerializer
from questions_app.models import (MultipleChoice, ApplicantScore,
    ApplicantAnswer, Question)
from questions_app.serializers import (MultipleChoiceSerializer, 
    ApplicantScoreSerializer, ApplicantAnswerSerializer,
    QuestionSerializer)
from organization_address_app.serializers import (ContractSerializer, 
    OrganizationProfileSerializer, InvitationsSerializer)
from organization_address_app.models import Contract, OrganizationProfile, Invitations
from cv_app.serializers import (PersonalInformationSerializer, 
    EducationInformationSerializer, ExperienceInformationSerializer)
from cv_app.models import (PersonalInformation, EducationInformation,
    ExperienceInformation)
from certificate_app.models import Certificate
from certificate_app.serializers import CertificateSerializer

class InterviewScheduleByPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InterviewScheduleSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return InterviewSchedule.objects.filter(post=post_id)

class QuestionChoicesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = MultipleChoiceSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        question_id = self.kwargs.get('questionId')
        return MultipleChoice.objects.filter(question=question_id)

class QuestionsByProfessionsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        profession_id = self.kwargs.get('professionId')
        return Question.objects.filter(profession=profession_id)

class ApplicantMarksViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ApplicantScoreSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        post_id = self.kwargs.get('postId')
        return ApplicantScore.objects.filter(alumni=alumni_id, post=post_id)
        
class ApplicantAnswersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ApplicantAnswerSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        post_id = self.kwargs.get('postId')
        return ApplicantAnswer.objects.filter(alumni=alumni_id, post=post_id)

        
class ProjectsByMemberViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProjectMemberSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        memberId = self.kwargs.get('memberId')
        return ProjectMember.objects.filter(member=memberId)

class ProjectMembersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProjectMemberSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        projectId = self.kwargs.get('projectId')
        return ProjectMember.objects.filter(project=projectId)

class AnnouncementsByDesignationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AnnouncementSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        designation_id = self.kwargs.get('designationId')
        return Announcement.objects.filter(destination=designation_id)

class UsersProfilesByDesignationIdViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        designation_id = self.kwargs.get('designationId')
        return UserProfile.objects.filter(designation=designation_id)

class SingleUserProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        user_id = self.kwargs.get('userId')
        return UserProfile.objects.filter(user=user_id)

class StudentProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfessionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        student_id = self.kwargs.get('studentId')
        return StudentProfession.objects.filter(student=student_id)

class StudentReportViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldReportSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        student_id = self.kwargs.get('studentId')
        return FieldReport.objects.filter(student=student_id)

class ProgramsByDepartmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProgramSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        department_id = self.kwargs.get('departmentId')
        return Program.objects.filter(department=department_id)

class StudentsByProgramViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        program_id = self.kwargs.get('programId')
        return StudentProfile.objects.filter(program=program_id)

class StudentsByOrganizationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return StudentProfile.objects.filter(organization=organization_id)

class SingleOrganizationProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = OrganizationProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return OrganizationProfile.objects.filter(organization_id=organization_id)

class StudentsByDepartmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        department_id = self.kwargs.get('departmentId')
        return StudentProfile.objects.filter(department=department_id)
        
class StudentsByAcademicSpervisorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        supervisor_id = self.kwargs.get('supervisorId')
        return StudentProfile.objects.filter(academic_supervisor=supervisor_id)
        
class StudentsByFieldSpervisorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        supervisor_id = self.kwargs.get('supervisorId')
        return StudentProfile.objects.filter(field_supervisor=supervisor_id)

class StudentsByStatusViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        status = self.kwargs.get('status')
        return StudentProfile.objects.filter(student_status=status)

class StudentsByYearOfStudyViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        year = self.kwargs.get('year')
        return StudentProfile.objects.filter(year_of_study=year)

class ReportedStudentsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        return FieldApplication.objects.filter(has_reported=True)

class ReportedStudentsProfilesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        return StudentProfile.objects.filter(has_reported=True)

class SingleStudentProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        student_id = self.kwargs.get('studentId')
        return StudentProfile.objects.filter(student=student_id)


class AlumniProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfessionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return AlumniProfession.objects.filter(alumni=alumni_id)

class PubllishedAlumniViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PublishedAlumniSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        return AlumniProfile.objects.filter(is_public=True)

class CvPersonalInformationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PersonalInformationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return PersonalInformation.objects.filter(alumni=alumni_id)

class CvEducationInformationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = EducationInformationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return EducationInformation.objects.filter(alumni=alumni_id)

class CvExperienceInformationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ExperienceInformationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return ExperienceInformation.objects.filter(alumni=alumni_id)

class AlumniCertificatesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CertificateSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return Certificate.objects.filter(alumni=alumni_id)

class SingleAlumniProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return AlumniProfile.objects.filter(alumni=alumni_id)

class SingleStaffProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StaffProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        staff_id = self.kwargs.get('staffId')
        return StaffProfile.objects.filter(staff=staff_id)

class OrganizationContractsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ContractSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return Contract.objects.filter(organization=organization_id)

class AlumniByOrganizationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return AlumniProfile.objects.filter(organization=organization_id)

class AlumniByCompletionYearViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        year = self.kwargs.get('year')
        return AlumniProfile.objects.filter(completion_year=year)


class AlumniByDegreeProgramViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        program_id = self.kwargs.get('programId')
        return AlumniProfile.objects.filter(program=program_id)

class AlumniByDepartmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        department_id = self.kwargs.get('departmentId')
        return AlumniProfile.objects.filter(department=department_id)

class FieldPostByOrganizationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldPostSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return FieldPost.objects.filter(organization=organization_id)

class FieldProfessionByPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldPostProfessionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return FieldPostProfession.objects.filter(post=post_id)

class FieldProgramByPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldPostProgramSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return FieldPostProgram.objects.filter(post=post_id)

class FieldApplicationByPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return FieldApplication.objects.filter(post=post_id)

class FieldApplicationByStudentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        student_id = self.kwargs.get('studentId')
        return FieldApplication.objects.filter(student=student_id)

class InternshipPostByOrganizationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InternshipPostSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return InternshipPost.objects.filter(organization=organization_id)
        
class InternshipApplicationByOrganizationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InternshipApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return InternshipApplication.objects.filter(organization=organization_id, status="accepted")

class InternshipApplicationByPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InternshipApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return InternshipApplication.objects.filter(post=post_id)


class InternshipApplicationByAlumniViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InternshipApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return InternshipApplication.objects.filter(alumni=alumni_id)

class AlumniByStatusViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        status = self.kwargs.get('status')
        return AlumniProfile.objects.filter(is_active=status)


     
class AlumniInvitationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InvitationsSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return Invitations.objects.filter(alumni=alumni_id)


class OrganizationInvitationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InvitationsSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        organization_id = self.kwargs.get('organizationId')
        return Invitations.objects.filter(organization=organization_id)



        