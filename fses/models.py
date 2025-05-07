from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    PROFESSOR = 1
    ASSOCIATE_PROFESSOR = 2
    DOCTOR = 3
    TITLE_CHOICES = [
        (PROFESSOR, "Professor"),
        (ASSOCIATE_PROFESSOR, "Associate Professor"),
        (DOCTOR, "Doctor"),
    ]

    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.IntegerField(choices=TITLE_CHOICES, default=DOCTOR)
    university = models.CharField(max_length=30)
    staff = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    PHD = "PHD"
    MPHIL = "MPHIL"
    DSE = "DSE"
    PROGRAM_CHOICES = [
        (PHD, "PhD"),
        (MPHIL, "MPhil"),
        (DSE, "DSE"),
    ]

    FIRST_EVALUATION = "FIRST_EVALUATION"
    RE_EVALUATION = "RE_EVALUATION"
    EVALUATION_CHOICES = [
        (FIRST_EVALUATION, "First Evaluation"),
        (RE_EVALUATION, "Re-Evaluation"),
    ]

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
    program = models.CharField(max_length=10, choices=PROGRAM_CHOICES, default=PHD)
    semester = models.PositiveSmallIntegerField(default=1)
    evaluation_type = models.CharField(
        choices=EVALUATION_CHOICES, default=FIRST_EVALUATION
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Nomination(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    examiner1 = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        related_name="examiner_1_id",
    )
    examiner2 = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        related_name="examiner_2_id",
    )
    examiner3 = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        related_name="examiner_3_id",
    )
    research_title = models.CharField(max_length=150, blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    chairperson = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        related_name="chairperson_id",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.student.name} - {self.research_title}"
