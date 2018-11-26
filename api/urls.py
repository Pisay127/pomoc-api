from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import CreateStudentCharacterRatingCriteriaView
from api.views import StudentCharacterRatingCriteriaView


urlpatterns = format_suffix_patterns([
    path('student-character-rating-criteria/',
         CreateStudentCharacterRatingCriteriaView.as_view(),
         name='create_student_character_rating_criteria'),
    path('student-character-rating-criteria/<int:pk>/',
         StudentCharacterRatingCriteriaView.as_view(),
         name='student_character_rating_criteria')
])