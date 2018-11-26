from django.db import models


class Base(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class StudentCharacterRatingCriteria(Base):
    name = models.TextField('Name',
                            null=False,
                            blank=False,
                            unique=True)

    def __str__(self):
        return '<StudentCharacterRatingCriteria {}>'.format(self.name)


class StudentMonthlyRequiredDays(Base):
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


class Batch(Base):
    year = models.PositiveSmallIntegerField('Year',
                                            null=False,
                                            blank=False,
                                            unique=True)

    def __str__(self):
        return '<Batch {}>'.format(self.year)


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


class PossibleTeacherPosition(Base):
    name = models.TextField('Name',
                            null=False,
                            blank=False,
                            unique=True)

    def __str__(self):
        return '<PossibleTeacherPosition {}'.format(self.name)
