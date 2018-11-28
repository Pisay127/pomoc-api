from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from api.helpers import RandomFileName
from api.helpers import ChoiceEnum


class Base(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class User(Base, AbstractUser):
    # Remember that Django being Django,certain user fields such as
    # usernames and email addresses have already been implemented by the
    # AbstractUser class.
    class UserTypes(ChoiceEnum):
        STUDENT = 'student'
        TEACHER = 'teacher'
        ADMIN = 'admin'

    user_type = models.CharField('User Type',
                                 max_length=7,
                                 choices=UserTypes.get_choices(),
                                 null=False,
                                 blank=False)

    middle_name = models.TextField('Middle Name',
                                   null=False,  # Following the first and last
                                                # names inside AbstractUser.
                                   blank=True)
    birth_date = models.DateField('Birth Date',
                                  null=True,
                                  blank=True)

    avatar = models.ImageField('Avatar',
                               null=True,
                               blank=True,
                               upload_to=RandomFileName('images/avatars/'))

    @property
    def age(self):
        today = date.today()
        today_monthday = (today.month, today.day)
        birth_date_monthday = (self.birth_date.month, self.birth_date.day)
        tentative_age = today.year - self.birth_date.year
        is_today_behind_birth_date = today_monthday < birth_date_monthday

        return tentative_age - int(is_today_behind_birth_date)


class Student(Base):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    year_level = models.PositiveSmallIntegerField('Year Level',
                                                  null=True,
                                                  blank=False)


class StudentStatus(Base):
    student_id = models.ForeignKey(Student,
                                   on_delete=models.CASCADE)
    status = models.TextField('Status',
                              null=False,
                              blank=False)
    quarter = models.PositiveSmallIntegerField('Quarter',
                                               null=False,
                                               blank=False)
    year_level = models.PositiveSmallIntegerField('Year Level',
                                                  null=False,
                                                  blank=False)
    school_year = models.TextField('School Year',
                                   null=False,
                                   blank=False)


class StudentMonthlyRequiredDays(Base):
    # TODO: Change school_year to start_year and end_year.
    month = models.PositiveSmallIntegerField('Month',
                                             null=False,
                                             blank=False)
    school_year = models.TextField('School Year',
                                   null=False,
                                   blank=False)
    num_days = models.PositiveSmallIntegerField('Required Number of Days',
                                                null=False,
                                                blank=True)

    def __str__(self):
        return '<StudentMonthlyRequiredDays {} {}>'.format(self.month,
                                                           self.school_year)


    class Meta:
        unique_together = (('month', 'school_year'),)


class StudentMonthlyAttendance(Base):
    student_id = models.ForeignKey(Student,
                                   on_delete=models.CASCADE)
    monthly_required_days_id = models.ForeignKey(StudentMonthlyRequiredDays,
                                                 on_delete=models.PROTECT)
    quarter = models.PositiveSmallIntegerField('Quarter',
                                               null=False,
                                               blank=False)
    year_level = models.PositiveSmallIntegerField('Year Level',
                                                  null=False,
                                                  blank=False)
    days_present = models.PositiveSmallIntegerField('Days Present',
                                                    null=False,
                                                    blank=False)
    days_tardy = models.PositiveSmallIntegerField('Days Tardy',
                                                  null=False,
                                                  blank=False)
    days_absent = models.PositiveSmallIntegerField('Days Absent',
                                                   null=False,
                                                   blank=False)


class Section(Base):
    name = models.TextField('Name',
                            null=False,
                            blank=False,
                            unique=True)
    year_level = models.PositiveSmallIntegerField('Year Level',
                                                  null=False,
                                                  blank=False)

    def __str__(self):
        return '<Section {} - {}>'.format(self.name, self.year_level)


class StudentSection(Base):
    student_id = models.ForeignKey(Student,
                                   on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section,
                                   on_delete=models.PROTECT)
    school_year = models.TextField('School Year',
                                   null=False,
                                   blank=False)


class StudentCharacterRatingCriteria(Base):
    name = models.TextField('Name',
                            null=False,
                            blank=False,
                            unique=True)

    def __str__(self):
        return '<StudentCharacterRatingCriteria {}>'.format(self.name)


class StudentRating(Base):
    student_id = models.ForeignKey(Student,
                                   on_delete=models.CASCADE)
    criterion_id = models.ForeignKey(StudentCharacterRatingCriteria,
                                     on_delete=models.PROTECT)
    rating = models.CharField('Rating',
                              max_length=1,
                              null=False,
                              blank=False)
    quarter = models.PositiveSmallIntegerField('Quarter',
                                               null=False,
                                               blank=False)
    year_level = models.PositiveSmallIntegerField('Year Level',
                                                  null=False,
                                                  blank=False)
    school_year = models.TextField('School Year',
                                   null=False,
                                   blank=False)


class Batch(Base):
    year = models.PositiveSmallIntegerField('Year',
                                            null=False,
                                            blank=False,
                                            unique=True)

    def __str__(self):
        return '<Batch {}>'.format(self.year)


class StudentBatch(Base):
    student_id = models.ForeignKey(Student,
                                   on_delete=models.CASCADE)
    batch_id = models.ForeignKey(Batch,
                                 on_delete=models.PROTECT)


class Subject(Base):
    name = models.TextField('Name',
                            null=False,
                            blank=False,
                            unique=True)
    year_level = models.PositiveSmallIntegerField('Year Level',
                                                  null=False,
                                                  blank=False)

    def __str__(self):
        return '<Subject {} ({})>'.format(self.name, self.year_level)


class Teacher(Base):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)


class PossibleTeacherPosition(Base):
    name = models.TextField('Name',
                            null=False,
                            blank=False,
                            unique=True)

    def __str__(self):
        return '<PossibleTeacherPosition {}'.format(self.name)


class Admin(Base):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
