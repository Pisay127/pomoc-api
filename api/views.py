from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializers import *


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateStudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentStatusView(generics.ListCreateAPIView):
    queryset = StudentStatus.objects.all()
    serializer_class = StudentStatusSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentStatusView(generics.ListCreateAPIView):
    queryset = StudentStatus.objects.all()
    serializer_class = StudentStatusSerializer


class CreateStudentCharacterRatingCriteriaView(generics.ListCreateAPIView):
    queryset = StudentCharacterRatingCriteria.objects.all()
    serializer_class = StudentCharacterRatingCriteriaSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentCharacterRatingCriteriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentCharacterRatingCriteria.objects.all()
    serializer_class = StudentCharacterRatingCriteriaSerializer


class CreateStudentMonthlyAttendanceView(generics.ListCreateAPIView):
    queryset = StudentMonthlyAttendance.objects.all()
    serializer_class = StudentMonthlyAttendanceSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentMonthlyAttendanceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentMonthlyAttendance.objects.all()
    serializer_class = StudentMonthlyAttendanceSerializer


class CreateStudentSectionView(generics.ListCreateAPIView):
    queryset = StudentSection.objects.all()
    serializer_class = StudentSectionSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentSectionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSection.objects.all()
    serializer_class = StudentSectionSerializer


class CreateStudentRatingView(generics.ListCreateAPIView):
    queryset = StudentRating.objects.all()
    serializer_class = StudentRatingSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentRatingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentRating.objects.all()
    serializer_class = StudentRatingSerializer


class CreateStudentBatchView(generics.ListCreateAPIView):
    queryset = StudentBatch.objects.all()
    serializer_class = StudentBatchSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentBatchView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentBatch.objects.all()
    serializer_class = StudentBatchSerializer


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


class CreateSubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        serializer.save()


class SubjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CreateTeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        serializer.save()


class TeacherView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CreatePossibleTeacherPositionView(generics.ListCreateAPIView):
    queryset = PossibleTeacherPosition.objects.all()
    serializer_class = PossibleTeacherPositionSerializer

    def perform_create(self, serializer):
        serializer.save()


class PossibleTeacherPositionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PossibleTeacherPosition.objects.all()
    serializer_class = PossibleTeacherPositionSerializer


class CreateTeacherPositionView(generics.ListCreateAPIView):
    queryset = TeacherPosition.objects.all()
    serializer_class = TeacherPositionSerializer

    def perform_create(self, serializer):
        serializer.save()


class TeacherPositionView(generics.ListCreateAPIView):
    queryset = TeacherPosition.objects.all()
    serializer_class = TeacherPositionSerializer


class CreateSectionAdvisorView(generics.ListCreateAPIView):
    queryset = SectionAdvisor.objects.all()
    serializer_class = SectionAdvisorSerializer

    def perform_create(self, serializer):
        serializer.save()


class SectionAdvisorView(generics.ListCreateAPIView):
    queryset = SectionAdvisor.objects.all()
    serializer_class = SectionAdvisorSerializer


class CreateBatchAdvisorView(generics.ListCreateAPIView):
    queryset = BatchAdvisor.objects.all()
    serializer_class = BatchAdvisorSerializer

    def perform_create(self, serializer):
        serializer.save()


class BatchAdvisorView(generics.ListCreateAPIView):
    queryset = BatchAdvisor.objects.all()
    serializer_class = BatchAdvisorSerializer


class CreateSubjectOfferingView(generics.ListCreateAPIView):
    queryset = SubjectOffering.objects.all()
    serializer_class = SubjectOfferingSerializer

    def perform_create(self, serializer):
        serializer.save()


class SubjectOfferingView(generics.ListCreateAPIView):
    queryset = SubjectOffering.objects.all()
    serializer_class = SubjectOfferingSerializer


class CreateAdminView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def perform_create(self, serializer):
        serializer.save()


class AdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
