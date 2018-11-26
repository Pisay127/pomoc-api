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


class StudentCharacterRatingCriteriaTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            'name': 'Some Criterion'
        }
        self.create_response = self.client.post(reverse('create_student_'
                                                        + 'character_rating'
                                                        + '_criterion'),
                                                self.data,
                                                format='json')

    def test_api_can_create_a_criterion(self):
        self.assertEqual(self.create_response.status_code,
                         status.HTTP_201_CREATED)


class StudentMonthlyRequiredDaysTestCase(TestCase):
    pass


class SectionTestCase(TestCase):
    pass


class BatchTestCase(TestCase):
    pass


class SubjectTestCase(TestCase):
    pass


class PossibleTeacherPositionTestCase(TestCase):
    pass
