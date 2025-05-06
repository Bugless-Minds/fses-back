from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.IntegerChoices("Title", "PROFESSOR ASSOCIATE_PROFESSOR DOCTOR")
    university = models.CharField(max_length=30)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    supervisor = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="supervisor_id",
    )
    co_supervisor = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="co_supervisor_id",
    )
    program = models.TextChoices("Program", "PHD MPHIL DSE")
    semester = models.SmallIntegerField()
    evaluation_type = models.TextChoices(
        "Evaluation Type", "FIRST_EVALUATION RE-EVALUATION"
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Nomination(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    examiner1 = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True, related_name="examiner_1_id"
    )
    examiner2 = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True, related_name="examiner_2_id"
    )
    examiner3 = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True, related_name="examiner_3_id"
    )
    research_title = models.CharField(max_length=150)
    is_locked = models.BooleanField(default=False)
    chairperson = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True, related_name="chairperson_id"
    )

    def __str__(self):
        return f"{self.student.name} - {self.research_title}"
