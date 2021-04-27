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
from internship_post_app.models import InternshipApplication, InternshipPost, InternshipPostProfession
from internship_post_app.serializers import InternshipPostSerializer, InternshipPostProfessionSerializer, InternshipApplicationSerializer


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
        

class InternshipPostProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = InternshipPostProfessionSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return InternshipPostProfession.objects.filter(post=post_id)


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