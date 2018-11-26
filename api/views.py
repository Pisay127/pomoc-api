from django.shortcuts import render
from rest_framework import generics
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


class CreateStudentCharacterRatingCriteriaView(generics.ListCreateAPIView):
    queryset = StudentCharacterRatingCriteria.objects.all()
    serializer_class = StudentCharacterRatingCriteriaSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentCharacterRatingCriteriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentCharacterRatingCriteria.objects.all()
    serializer_class = StudentCharacterRatingCriteriaSerializer


class CreateStudentMonthlyRequiredDaysView(generics.ListCreateAPIView):
    queryset = StudentMonthlyRequiredDays.objects.all()
    serializer_class = StudentMonthlyRequiredDaysSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentMonthlyRequiredDaysView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentMonthlyRequiredDays.objects.all()
    serializer_class = StudentMonthlyRequiredDaysSerializer


class CreateSectionView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_create(self, serializer):
        serializer.save()


class SectionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CreateBatchView(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def perform_create(self, serializer):
        serializer.save()


class BatchView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer