from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import CreateStudentCharacterRatingCriteriaView
from api.views import StudentCharacterRatingCriteriaView
from api.views import CreateStudentMonthlyRequiredDaysView
from api.views import StudentMonthlyRequiredDaysView
from api.views import CreateSectionView
from api.views import SectionView
from api.views import CreateBatchView
from api.views import BatchView


urlpatterns = format_suffix_patterns([
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
    path('batch/<int:pk>/', BatchView.as_view(), name='batch')
])