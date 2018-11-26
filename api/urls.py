from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import CreateStudentCharacterRatingCriteriaView


urlpatterns = format_suffix_patterns([
    path('student-character-rating-criteria/',
         CreateStudentCharacterRatingCriteriaView.as_view(),
         name='create_student_character_rating_criterion'),
])