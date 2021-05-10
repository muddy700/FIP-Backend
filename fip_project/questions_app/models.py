from profession_app.models import Profession
from django.db import models
from django.contrib.auth.models import User
from internship_post_app.models import InternshipPost

class Question(models.Model):
    question_body = models.CharField(max_length=500)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_body

class MultipleChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=500)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.choice

class ApplicantScore(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(InternshipPost, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'{self.alumni.username} Marks'


class ApplicantAnswer(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    post = models.ForeignKey(InternshipPost, on_delete=models.CASCADE)
    choice = models.ForeignKey(MultipleChoice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.alumni.username} Choice'

