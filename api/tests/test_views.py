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
    pass


class BatchTestCase(TestCase):
    pass


class SubjectTestCase(TestCase):
    pass


class PossibleTeacherPositionTestCase(TestCase):
    pass
