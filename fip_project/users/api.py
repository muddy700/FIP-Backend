from datetime import date
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404, get_list_or_404
from student_profile_app.models import StudentProfession

router = Router()

class UserSchema(Schema):
    id: int
    username: str
class ProfessionSchema(Schema):
    id: int
    profession_name: str
    
class ProfessionOut(Schema):
    id: int
    student: UserSchema
    profession: ProfessionSchema

# Todo Filters
@router.get("/student-professions/{student_id}", response=List[ProfessionOut], tags=["Profession-Filters"])
def list_student_professions(request, student_id: int):
    qs = StudentProfession.objects.filter(student=student_id)
    return qs