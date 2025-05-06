from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)


class Lecturer(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.IntegerChoices("Title", "PROFESSOR ASSOCIATE_PROFESSOR DOCTOR")
    university = models.CharField(max_length=30)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Student(models.Model):
    name = models.CharField(max_length=50)
    supervisor = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, blank=True, null=True
    )
    co_supervisor = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, blank=True, null=True
    )
    program = models.TextChoices("Program", "PHD MPHIL DSE")
    semester = models.SmallIntegerField(max_length=2)
    evaluation_type = models.TextChoices(
        "Evaluation Type", "FIRST_EVALUATION RE-EVALUATION"
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Nomination(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    examiner1 = models.ForeignKey(Lecturer, on_delete=models.SET_NULL)
    examiner2 = models.ForeignKey(Lecturer, on_delete=models.SET_NULL)
    examiner3 = models.ForeignKey(Lecturer, on_delete=models.SET_NULL)
    research_title = models.CharField(max_length=150)
    is_locked = models.BooleanField(default=False)
    chairperson = models.ForeignKey(Lecturer, on_delete=models.SET_NULL)
