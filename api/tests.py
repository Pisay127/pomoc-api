from django.test import TestCase
from django.db import IntegrityError
from api.models import Section
from api.models import Batch


class SectionModelTestCase(TestCase):
    def setUp(self):
        self.section_name = 'Section'
        self.section = Section(name=self.section_name, year_level=1)

    def test_can_create_a_section_properly(self):
        preaddition_count = Section.objects.count()
        self.section.save()

        postaddition_count = Section.objects.count()

        try:
            new_section = Section.objects.get(name=self.section_name)
        except Section.DoesNotExist:
            self.fail('Exception occured. '
                      + 'Unable to get a Section object with section name '
                      + '{}.'.format(self.section_name))
        
        self.assertNotEqual(preaddition_count, postaddition_count)
        self.assertEqual(new_section.year_level, 1)
        # No need to check if the section name is correct because we won't get
        # any records from the Section table if the section name is different
        # from the section name of the record we want.

    def test_should_not_create_a_section_with_non_unique_name(self):
        Section(name='Section1', year_level=1).save()
        self.assertRaises(IntegrityError,
                          Section(name='Section1', year_level=1).save)



class BatchModelTestCase(TestCase):
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
                      + 'Unable to get a Batch object with year ' 
                      + '{}.'.format(self.batch_year))

        self.assertNotEqual(preaddition_count, postaddition_count)

    def test_should_create_a_batch_with_non_unique_year(self):
        Batch(year=2018).save()
        self.assertRaises(IntegrityError, Batch(year=2018).save)
