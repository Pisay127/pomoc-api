from rest_framework import serializers
from api.models import StudentCharacterRatingCriteria
from api.models import StudentMonthlyRequiredDays
from api.models import Section
from api.models import Batch
from api.models import Subject
from api.models import PossibleTeacherPosition


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('date_created', 'date_modified')


class StudentCharacterRatingCriteriaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentCharacterRatingCriteria
        fields = ('id', 'name', 'date_created', 'date_modified',)


class StudentMonthlyRequiredDaysSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentMonthlyRequiredDays
        fields = ('id',
                  'month',
                  'school_year',
                  'num_days',
                  'date_created',
                  'date_modified',)


class SectionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Section
        fields = ('id', 'name', 'year_level', 'date_created', 'date_modified',)


class BatchSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Batch
        fields = ('id', 'year', 'date_created', 'date_modified',)


class SubjectSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Subject
        fields = ('id', 'name', 'year_level', 'date_created', 'date_modified',)


class PossibleTeacherPositionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = PossibleTeacherPosition
        fields = ('id', 'name', 'date_created', 'date_modified',)
