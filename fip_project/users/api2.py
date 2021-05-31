from rest_framework import permissions
from rest_framework import viewsets, mixins

from student_profile_app.serializers import StudentProfessionSerializer, StudentProfileSerializer, FieldReportSerializer
from alumni_profile_app.serializers import AlumniProfileSerializer, AlumniProfessionSerializer
from student_profile_app.models import StudentProfession, StudentProfile, FieldReport
from alumni_profile_app.models import AlumniProfile, AlumniProfession
from program_app.serializers import ProgramSerializer
from program_app.models import Program
from field_post_app.models import FieldApplication, FieldPost, FieldPostProfession
from field_post_app.serializers import FieldPostProfessionSerializer, FieldApplicationSerializer, FieldPostSerializer
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
from organization_address_app.serializers import ContractSerializer
from organization_address_app.models import Contract

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


class AlumniProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfessionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return AlumniProfession.objects.filter(alumni=alumni_id)

class SingleAlumniProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AlumniProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        alumni_id = self.kwargs.get('alumniId')
        return AlumniProfile.objects.filter(alumni=alumni_id)

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

class FieldPostProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FieldPostProfessionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return FieldPostProfession.objects.filter(post=post_id)

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