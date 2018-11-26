from django.test import TestCase
from django.db import IntegrityError
from api.models import StudentCharacterRatingCriteria
from api.models import StudentMonthlyRequiredDays
from api.models import Section
from api.models import Batch
from api.models import Subject
from api.models import PossibleTeacherPosition


class StudentCharacterRatingCriteriaTestCase(TestCase):
    def setUp(self):
        self.criterion_name = 'Criterion'
        self.criterion = StudentCharacterRatingCriteria(
                             name=self.criterion_name)

    def test_can_create_a_criterion_properly(self):
        preaddition_count = StudentCharacterRatingCriteria.objects.count()
        self.criterion.save()

        postaddition_count = StudentCharacterRatingCriteria.objects.count()

        try:
            new_criterion = StudentCharacterRatingCriteria.objects.get(
                                name=self.criterion_name
                            )
        except StudentCharacterRatingCriteria.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a StudentCharacterRatingCriteria object '
                      + 'with criterion name "{}".'.format(self.section_name))

        self.assertNotEqual(preaddition_count, postaddition_count)
        self.assertEqual(new_criterion.name, self.criterion_name)

    def test_should_not_create_criterion_with_preexisting_name(self):
        StudentCharacterRatingCriteria(name='Criterion 1').save()
        self.assertRaises(IntegrityError,
                          StudentCharacterRatingCriteria(
                                name='Criterion 1').save)


class StudentMonthlyRequiredDaysTestCase(TestCase):
    def setUp(self):
        self.month = 1
        self.school_year = '2018-2019'
        self.num_days = 1
        self.monthly_required_days = StudentMonthlyRequiredDays(
                                         month=self.month,
                                         school_year=self.school_year,
                                         num_days=self.num_days)

    def test_can_create_a_monthly_required_days_properly(self):
        preaddition_count = StudentMonthlyRequiredDays.objects.count()
        self.monthly_required_days.save()

        postaddition_count = StudentMonthlyRequiredDays.objects.count()

        try:
            new_monthly_required_days = StudentMonthlyRequiredDays.objects.get(
                                            month=self.month,
                                            school_year=self.school_year)
        except StudentMonthlyRequiredDays.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a StudentMonthlyRequiredDays object for '
                      + '{} {}.'.format(self.month, self.school_year))

        self.assertNotEqual(preaddition_count, postaddition_count)
        self.assertEqual(new_monthly_required_days.num_days, self.num_days)

    def test_should_not_create_a_nonunique_monthly_required_days(self):
        StudentMonthlyRequiredDays(month=1,
                                   school_year='2015-2016',
                                   num_days=30).save()
        self.assertRaises(IntegrityError,
                          StudentMonthlyRequiredDays(month=1,
                                                     school_year='2015-2016',
                                                     num_days=30).save)


class SectionTestCase(TestCase):
    def setUp(self):
        self.section_name = 'Section'
        self.section_year_level = 1
        self.section = Section(name=self.section_name,
                               year_level=self.section_year_level)

    def test_can_create_a_section_properly(self):
        preaddition_count = Section.objects.count()
        self.section.save()

        postaddition_count = Section.objects.count()

        try:
            new_section = Section.objects.get(name=self.section_name)
        except Section.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a Section object with section name '
                      + '"{}".'.format(self.section_name))
        
        self.assertNotEqual(preaddition_count, postaddition_count)
        self.assertEqual(new_section.year_level, self.section_year_level)
        # No need to check if the section name is correct because we won't get
        # any records from the Section table if the section name is different
        # from the section name of the record we want.

    def test_should_not_create_a_section_with_preexisting_name(self):
        Section(name='Section1', year_level=1).save()
        self.assertRaises(IntegrityError,
                          Section(name='Section1', year_level=1).save)



class BatchTestCase(TestCase):
    def setUp(self):
        self.batch_year = 2015
        self.batch = Batch(year=self.batch_year)

    def test_can_create_a_batch_properly(self):
        preaddition_count = Batch.objects.count()
        self.batch.save()

        postaddition_count = Batch.objects.count()

        try:
            new_batch = Batch.objects.get(year=self.batch_year)
        except Batch.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a Batch object of year ' 
                      + '{}.'.format(self.batch_year))

        self.assertNotEqual(preaddition_count, postaddition_count)

    def test_should_not_create_a_batch_with_preexisting_year(self):
        Batch(year=2018).save()
        self.assertRaises(IntegrityError, Batch(year=2018).save)


class SubjectTestCase(TestCase):
    def setUp(self):
        self.subject_name = 'Subject'
        self.year_level = 1
        self.subject = Subject(name=self.subject_name,
                               year_level=self.year_level)

    def test_can_create_a_subject_properly(self):
        preaddition_count = Subject.objects.count()
        self.subject.save()

        postaddition_count = Subject.objects.count()

        try:
            new_subject = Subject.objects.get(name=self.subject_name)
        except Subject.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a Subject object with name '
                      + '"{}".'.format(self.self.subject_name))

        self.assertNotEqual(preaddition_count, postaddition_count)

    def test_should_not_create_a_subject_with_preexisting_name(self):
        Subject(name='Subject', year_level=1).save()
        self.assertRaises(IntegrityError,
                          Subject(name='Subject', year_level=1).save)


class PossibleTeacherPositionTestCase(TestCase):
    def setUp(self):
        self.position_name = 'Position'
        self.possible_teacher_position = PossibleTeacherPosition(
                                             name=self.position_name)

    def test_can_create_a_possible_teacher_position(self):
        preaddition_count = PossibleTeacherPosition.objects.count()
        self.possible_teacher_position.save()

        postaddition_count = PossibleTeacherPosition.objects.count()

        try:
            new_position = PossibleTeacherPosition.objects.get(
                               name=self.position_name)
        except PossibleTeacherPosition.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a PossibleTeacherPosition object with '
                      + 'name "{}".'.format(self.self.position_name))

        self.assertNotEqual(preaddition_count, postaddition_count)

    def test_should_not_create_position_with_preexisting_name(self):
        PossibleTeacherPosition(name='Position').save()
        self.assertRaises(IntegrityError,
                          PossibleTeacherPosition(name='Position').save)

