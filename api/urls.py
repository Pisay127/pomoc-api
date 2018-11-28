from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *


urlpatterns = format_suffix_patterns([
    path('user/', UsersView.as_view(), name='users'),
    path('user/<int:pk>', UserView.as_view(), name='user'),
    path('user/student/', CreateStudentView.as_view(), name='create_student'),
    path('user/student/<int:pk>/', StudentView.as_view(), name='student'),
    path('student-character-rating-criteria/',
         CreateStudentCharacterRatingCriteriaView.as_view(),
         name='create_student_character_rating_criteria'),
    path('student-character-rating-criteria/<int:pk>/',
         StudentCharacterRatingCriteriaView.as_view(),
         name='student_character_rating_criteria'),
    path('student-monthly-required-days/',
         CreateStudentMonthlyRequiredDaysView.as_view(),
         name='create_student_monthly_required_days'),
    path('student-monthly-required-days/<int:pk>/',
         StudentMonthlyRequiredDaysView.as_view(),
         name='student_monthly_required_days'),
    path('section/', CreateSectionView.as_view(), name='create_section'),
    path('section/<int:pk>/', SectionView.as_view(), name='section'),
    path('batch/', CreateBatchView.as_view(), name='create_batch'),
    path('batch/<int:pk>/', BatchView.as_view(), name='batch'),
    path('subject/', CreateSubjectView.as_view(), name='create_subject'),
    path('subject/<int:pk>/', SubjectView.as_view(), name='subject'),
    path('user/teacher/', CreateTeacherView.as_view(), name='create_teacher'),
    path('user/teacher/<int:pk>/', TeacherView.as_view(), name='teacher'),
    path('possible-teacher-position/',
         CreatePossibleTeacherPositionView.as_view(),
         name='create_possible_teacher_position'),
    path('possible-teacher-position/<int:pk>/',
         PossibleTeacherPositionView.as_view(),
         name='possible_teacher_position'),
    path('user/admin/', CreateAdminView.as_view(), name='create_admin'),
    path('user/admin/<int:pk>/', AdminView.as_view(), name='admin'),
])