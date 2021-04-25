from datetime import date
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404, get_list_or_404
from student_profile_app.models import StudentProfession
from program_app.models import Program
from student_profile_app.models import StudentProfile
from alumni_profile_app.models import AlumniProfile, AlumniProfession

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

class StudentsByYearOfStudy(Schema):
    id: int
    student: UserSchema

# Alumni Schemas

class ProfessionsOfAlumni(Schema):
    id: int
    alumni: UserSchema
    profession: ProfessionSchema

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