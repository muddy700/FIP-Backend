from datetime import date
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404, get_list_or_404
from program_app.models import Program
from student_profile_app.models import StudentProfile, FieldReport, StudentProfession
from alumni_profile_app.models import AlumniProfile, AlumniProfession
from field_post_app.models import FieldPost, FieldPostProfession, FieldApplication
from internship_post_app.models import InternshipApplication, InternshipPost, InternshipPostProfession

router = Router()

# General Schemas
class UserSchema(Schema):
    id: int
    username: str

class ProfessionSchema(Schema):
    id: int
    profession_name: str

class DepartmentSchema(Schema):
    id: int
    department_name: str
    
class ProgramSchema(Schema):
    id: int
    program_name: str

class PostSchema(Schema):
    id: int
    post_title: str

# Specific Schemas

# Programs Schemas

class ProgramsByDepartment(Schema):
    id: int
    program_name: str
    department: DepartmentSchema

# Student Schemas

class ProfessionsOfStudent(Schema):
    id: int
    student: UserSchema
    profession: ProfessionSchema

class ReportSchema(Schema):
    id: int
    student: UserSchema
    report_file: str

class StudentApplications(Schema):
    id: int
    student: UserSchema
    post: PostSchema

class StudentsByProgram(Schema):
    id: int
    program: ProgramSchema
    student: UserSchema

class StudentsByDepartment(Schema):
    id: int
    student: UserSchema
    department: DepartmentSchema

class StudentsByAcademicSupervisor(Schema):
    id: int
    student: UserSchema
    academic_supervisor: UserSchema

class StudentsByFieldSupervisor(Schema):
    id: int
    student: UserSchema
    field_supervisor: UserSchema

class StudentsByStatus(Schema):
    id: int
    student: UserSchema
    student_status: bool

class StudentsByOrganization(Schema):
    id: int
    student: UserSchema
    organization: UserSchema
class StudentsByYearOfStudy(Schema):
    id: int
    student: UserSchema

# Alumni Schemas

class ProfessionsOfAlumni(Schema):
    id: int
    alumni: UserSchema
    profession: ProfessionSchema
class AlumniApplicationSchema(Schema):
    id: int
    alumni: UserSchema
    post: PostSchema
    status: str

class AlumniByOrganization(Schema):
    id: int
    alumni: UserSchema
    organization: UserSchema

class AlumniByStatus(Schema):
    id: int
    alumni: UserSchema
    is_active: bool

class AlumniByCompletionYear(Schema):
    id: int
    alumni: UserSchema
    completion_year: str

class AlumniByDegreeProgram(Schema):
    id: int
    alumni: UserSchema
    program: ProgramSchema

class AlumniByDepartment(Schema):
    id: int
    alumni: UserSchema
    department: DepartmentSchema


# Field Post Schemas
class PostByOrganization(Schema):
    id: int
    post_title: str
    organization: UserSchema

class PostProfessions(Schema):
    id: int
    post: PostSchema
    profession: ProfessionSchema

class FieldApplicationSchema(Schema):
    id: int
    post: PostSchema
    student: UserSchema

# Internship Post Schemas

class InternshipApplicationSchema(Schema):
    id: int
    post: PostSchema
    alumni: UserSchema
    status: str

@router.get("/student_professions/{student_id}", response=List[ProfessionsOfStudent], tags=["Student Professions"])
def list_student_professions(request, student_id: int):
    result = StudentProfession.objects.filter(student=student_id)
    return result

@router.get("/alumni_professions/{alumni_id}", response=List[ProfessionsOfAlumni], tags=["Alumni Professions"])
def list_alumni_professions(request, alumni_id: int):
    result = AlumniProfession.objects.filter(alumni=alumni_id)
    return result

@router.get("/programs_by_department/{department_id}", response=List[ProgramsByDepartment], tags=["Programs By Department"])
def list_programs_by_department(request, department_id: int):
    result = Program.objects.filter(department=department_id)
    return result

@router.get("/students_by_program/{program_id}", response=List[StudentsByProgram], tags=["Students By Program"])
def list_students_by_programs(request, program_id: int):
    result = StudentProfile.objects.filter(program=program_id)
    return result

@router.get("/students_by_department/{department_id}", response=List[StudentsByDepartment], tags=["Students By Department"])
def list_students_by_department(request, department_id: int):
    result = StudentProfile.objects.filter(department=department_id)
    return result

@router.get("/students_by_academic_supervisor/{supervisor_id}", response=List[StudentsByAcademicSupervisor], tags=["Students By Academic Supervisor"])
def list_students_by_academic_supervisor(request, supervisor_id: int):
    result = StudentProfile.objects.filter(academic_supervisor=supervisor_id)
    return result

@router.get("/students_by_field_supervisor/{supervisor_id}", response=List[StudentsByFieldSupervisor], tags=["Students By Field Supervisor"])
def list_students_by_field_supervisor(request, supervisor_id: int):
    result = StudentProfile.objects.filter(field_supervisor=supervisor_id)
    return result

@router.get("/students_by_status/{status}", response=List[StudentsByStatus], tags=["Students By Status"])
def list_students_by_status(request, status: bool):
    result = StudentProfile.objects.filter(student_status=status)
    return result

@router.get("/students_by_year_of_study/{year}", response=List[StudentsByYearOfStudy], tags=["Students By Year Of Study"])
def list_students_by_year_of_study(request, year: str):
    result = StudentProfile.objects.filter(year_of_study=year)
    return result

@router.get("/alumni_by_organization/{organization_id}", response=List[AlumniByOrganization], tags=["Alumni By Organization"])
def list_alumni_by_organization(request, organization_id: int):
    result = AlumniProfile.objects.filter(organization=organization_id)
    return result   

@router.get("/students_by_organization/{organization_id}", response=List[StudentsByOrganization], tags=["Students By Organization"])
def list_alumni_by_organization(request, organization_id: int):
    result = StudentProfile.objects.filter(organization=organization_id)
    return result   

@router.get("/alumni_by_status/{status}", response=List[AlumniByStatus], tags=["Alumni By Status"])
def list_alumni_by_status(request, status: bool):
    result = AlumniProfile.objects.filter(is_active=status)
    return result   

@router.get("/alumni_by_completion_year/{year}", response=List[AlumniByCompletionYear], tags=["Alumni By Completion Year"])
def list_alumni_by_completion_year(request, year: str):
    result = AlumniProfile.objects.filter(completion_year=year)
    return result   

@router.get("/alumni_by_degree_program/{program_id}", response=List[AlumniByDegreeProgram], tags=["Alumni By Degree Program"])
def list_alumni_by_degree_program(request, program_id: int):
    result = AlumniProfile.objects.filter(program=program_id)
    return result   

@router.get("/alumni_by_department/{department_id}", response=List[AlumniByDepartment], tags=["Alumni By Department"])
def list_alumni_by_department(request, department_id: int):
    result = AlumniProfile.objects.filter(department=department_id)
    return result   

@router.get("/field_posts_by_organization/{organization_id}", response=List[PostByOrganization], tags=["Field Posts By Organization"])
def list_field_posts_by_organization(request, organization_id: int):
    result = FieldPost.objects.filter(organization=organization_id)
    return result   

@router.get("/field_post_professions/{post_id}", response=List[PostProfessions], tags=["Field Post Professions"])
def list_field_post_professions(request, post_id: int):
    result = FieldPostProfession.objects.filter(post=post_id)
    return result   

@router.get("/field_post_applications/{post_id}", response=List[FieldApplicationSchema], tags=["Field Post Applications"])
def list_field_post_applications(request, post_id: int):
    result = FieldApplication.objects.filter(post=post_id)
    return result   

@router.get("/student_applications/{student_id}", response=List[StudentApplications], tags=["Student Applications"])
def list_student_applications(request, student_id: int):
    result = FieldApplication.objects.filter(student=student_id)
    return result   

@router.get("/internship_posts_by_organization/{organization_id}", response=List[PostByOrganization], tags=["Internship Posts By Organization"])
def list_internship_posts_by_organization(request, organization_id: int):
    result = InternshipPost.objects.filter(organization=organization_id)
    return result   

@router.get("/internship_post_professions/{post_id}", response=List[PostProfessions], tags=["Internship Post Professions"])
def list_internship_post_professions(request, post_id: int):
    result = InternshipPostProfession.objects.filter(post=post_id)
    return result 

@router.get("/internship_post_applications/{post_id}", response=List[InternshipApplicationSchema], tags=["Internship Post Applications"])
def list_internship_post_applications(request, post_id: int):
    result = InternshipApplication.objects.filter(post=post_id)
    return result 

@router.get("/alumni_applications/{alumni_id}", response=List[AlumniApplicationSchema], tags=["Alumni Applications"])
def list_alumni_applications(request, alumni_id: int):
    result = InternshipApplication.objects.filter(alumni=alumni_id)
    return result  

@router.get("/student_report/{student_id}", response=List[ReportSchema], tags=["Student Report"])
def list_student_report(request, student_id: int):
    result = FieldReport.objects.filter(student=student_id)
    return result   