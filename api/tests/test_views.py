from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import StudentCharacterRatingCriteria
from api.models import StudentMonthlyRequiredDays
from api.models import Section
from api.models import Batch
from api.models import Subject
from api.models import PossibleTeacherPosition
from api.serializers import StudentCharacterRatingCriteriaSerializer
from api.serializers import StudentMonthlyRequiredDaysSerializer
from api.serializers import SectionSerializer
from api.serializers import BatchSerializer
from api.serializers import SubjectSerializer
from api.serializers import PossibleTeacherPositionSerializer


class StudentCharacterRatingCriteriaTestCase(TestCase):
    def setUp(self):
        payload = {
            'name': 'Some Criterion'
        }
        self.client = APIClient()
        self.response = self.client.post(reverse('create_student_'
                                                 + 'character_rating'
                                                 + '_criteria'),
                                         payload,
                                         format='json')

    def test_api_can_create_a_criterion(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_cannot_create_invalid_criterion(self):
        payload = {
            'name': ''
        }
        response = self.client.post(reverse('create_student_character_rating_'
                                            + 'criteria'),
                                    payload,
                                    format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_can_get_a_criterion(self):
        criterion = StudentCharacterRatingCriteria.objects.get()
        response = self.client.get(reverse('student_character_rating_'
                                           + 'criteria',
                                            kwargs={
                                                'pk': criterion.id
                                            }),
                                   format='json')
        serialized_object = StudentCharacterRatingCriteriaSerializer(criterion)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_object.data)

    def test_api_cannot_get_invalid_criterion(self):
        response = self.client.get(reverse('student_character_rating_'
                                           + 'criteria',
                                            kwargs={
                                                # 0xFAE1BA10 = Fail Value :)
                                                'pk': 0xFAE1BA10
                                            }),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_update_a_criterion(self):
        payload = {
            'name': 'A New Criterion'
        }
        criterion = StudentCharacterRatingCriteria.objects.get()
        response = self.client.put(reverse('student_character_rating_'
                                           + 'criteria',
                                           kwargs={
                                              'pk': criterion.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_cannot_invalidly_update_a_criterion(self):
        payload = {
            'name': ''
        }
        criterion = StudentCharacterRatingCriteria.objects.get()
        response = self.client.put(reverse('student_character_rating_'
                                           + 'criteria',
                                           kwargs={
                                               'pk': criterion.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_delete_criterion(self):
        criterion = StudentCharacterRatingCriteria.objects.get()
        response = self.client.delete(reverse('student_character_rating_'
                                              + 'criteria',
                                              kwargs={
                                                  'pk': criterion.id
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_cannot_delete_invalid_criterion(self):
        response = self.client.delete(reverse('student_character_rating_'
                                              + 'criteria',
                                              kwargs={
                                                  # 0xFAE1BA10 = Fail Value :)
                                                  'pk': 0xFAE1BA10
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class StudentMonthlyRequiredDaysTestCase(TestCase):
    def setUp(self):
        payload = {
            'month': 1,
            'school_year': '2016-2017',
            'num_days': 30
        }
        self.client = APIClient()
        self.response = self.client.post(reverse('create_student_'
                                                 + 'monthly_required_days'),
                                         payload,
                                         format='json')

    def test_api_can_create_a_required_days_record(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_cannot_create_invalid_required_days_record(self):
        payload = {
            'month': 'May',
            'school_year': '2016-2017',
            'num_days': 30
        }
        response = self.client.post(reverse('create_student_monthly_required_'
                                            + 'days'),
                                    payload,
                                    format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_can_get_a_required_days_record(self):
        record = StudentMonthlyRequiredDays.objects.get()
        response = self.client.get(reverse('student_monthly_required_days',
                                            kwargs={
                                                'pk': record.id
                                            }),
                                   format='json')
        serialized_object = StudentMonthlyRequiredDaysSerializer(record)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_object.data)

    def test_api_cannot_get_invalid_required_days_record(self):
        response = self.client.get(reverse('student_monthly_required_days',
                                            kwargs={
                                                # 0xFAE1BA10 = Fail Value :)
                                                'pk': 0xFAE1BA10
                                            }),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_update_a_required_days_record(self):
        payload = {
            'month': 2,
            'school_year': '2016-2017',
            'num_days': 30
        }
        record = StudentMonthlyRequiredDays.objects.get()
        response = self.client.put(reverse('student_monthly_required_days',
                                           kwargs={
                                              'pk': record.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_cannot_invalidly_update_a_required_days_record(self):
        payload = {
            'month': 'May',
            'school_year': '2016-2017',
            'num_days': 30
        }
        record = StudentMonthlyRequiredDays.objects.get()
        response = self.client.put(reverse('student_monthly_required_days',
                                           kwargs={
                                               'pk': record.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_delete_required_days_record(self):
        record = StudentMonthlyRequiredDays.objects.get()
        response = self.client.delete(reverse('student_monthly_required_days',
                                              kwargs={
                                                  'pk': record.id
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_cannot_delete_invalid_required_days_record(self):
        response = self.client.delete(reverse('student_monthly_required_days',
                                              kwargs={
                                                  # 0xFAE1BA10 = Fail Value :)
                                                  'pk': 0xFAE1BA10
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SectionTestCase(TestCase):
    def setUp(self):
        payload = {
            'name': 'Section',
            'year_level': 4
        }
        self.client = APIClient()
        self.response = self.client.post(reverse('create_section'),
                                         payload,
                                         format='json')

    def test_api_can_create_a_section(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_cannot_create_invalid_section(self):
        payload = {
            'name': 'Section',
            'year_level': 'Four'
        }
        response = self.client.post(reverse('create_section'),
                                    payload,
                                    format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_can_get_a_section(self):
        section = Section.objects.get()
        response = self.client.get(reverse('section',
                                            kwargs={
                                                'pk': section.id
                                            }),
                                   format='json')
        serialized_object = SectionSerializer(section)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_object.data)

    def test_api_cannot_get_invalid_section(self):
        response = self.client.get(reverse('section',
                                            kwargs={
                                                # 0xFAE1BA10 = Fail Value :)
                                                'pk': 0xFAE1BA10
                                            }),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_update_a_section(self):
        payload = {
            'name': 'Section',
            'year_level': 1
        }
        section = Section.objects.get()
        response = self.client.put(reverse('section',
                                           kwargs={
                                              'pk': section.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_cannot_invalidly_update_a_section(self):
        payload = {
            'name': 'Section',
            'year_level': 'Four'
        }
        section = Section.objects.get()
        response = self.client.put(reverse('section',
                                           kwargs={
                                               'pk': section.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_delete_section(self):
        section = Section.objects.get()
        response = self.client.delete(reverse('section',
                                              kwargs={
                                                  'pk': section.id
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_cannot_delete_invalid_section(self):
        response = self.client.delete(reverse('section',
                                              kwargs={
                                                  # 0xFAE1BA10 = Fail Value :)
                                                  'pk': 0xFAE1BA10
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BatchTestCase(TestCase):
    def setUp(self):
        payload = {
            'year': 2015
        }
        self.client = APIClient()
        self.response = self.client.post(reverse('create_batch'),
                                         payload,
                                         format='json')

    def test_api_can_create_a_batch(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_cannot_create_invalid_batch(self):
        payload = {
            'year': '2015'
        }
        response = self.client.post(reverse('create_batch'),
                                    payload,
                                    format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_can_get_a_batch(self):
        batch = Batch.objects.get()
        response = self.client.get(reverse('batch',
                                            kwargs={
                                                'pk': batch.id
                                            }),
                                   format='json')
        serialized_object = BatchSerializer(batch)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_object.data)

    def test_api_cannot_get_invalid_batch(self):
        response = self.client.get(reverse('batch',
                                            kwargs={
                                                # 0xFAE1BA10 = Fail Value :)
                                                'pk': 0xFAE1BA10
                                            }),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_update_a_batch(self):
        payload = {
            'year': 2016
        }
        batch = Batch.objects.get()
        response = self.client.put(reverse('batch',
                                           kwargs={
                                              'pk': batch.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_cannot_invalidly_update_a_batch(self):
        payload = {
            'year': 'Twenty Fifteen'
        }
        batch = Batch.objects.get()
        response = self.client.put(reverse('batch',
                                           kwargs={
                                               'pk': batch.id
                                           }),
                                   payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_delete_batch(self):
        batch = Batch.objects.get()
        response = self.client.delete(reverse('batch',
                                              kwargs={
                                                  'pk': batch.id
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_cannot_delete_invalid_batch(self):
        response = self.client.delete(reverse('batch',
                                              kwargs={
                                                  # 0xFAE1BA10 = Fail Value :)
                                                  'pk': 0xFAE1BA10
                                              }),
                                      format='json',
                                      follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SubjectTestCase(TestCase):
    pass


class PossibleTeacherPositionTestCase(TestCase):
    pass
