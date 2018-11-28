from rest_framework import serializers
from api.models import *


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(BaseSerializer):
    # TODO: Add feature where the 'age' field is sent to the client too. At
    #       the moment, 'age' is not in the response.


    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'birth_date',
                  'email',
                  'age',
                  'avatar',)


class StudentSerializer(BaseSerializer):
    user = UserSerializer(many=False)


    class Meta:
        model = Student
        fields = ('year_level', 'user',)


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        student = Student.objects.create(**validated_data)
        User.objects.create(**user_data, user_type='student')

        return student


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


class TeacherSerializer(BaseSerializer):
    user = UserSerializer(many=False)


    class Meta:
        model = Teacher
        fields = ('user',)


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        teacher = Teacher.objects.create(**validated_data)
        User.objects.create(**user_data, user_type='teacher')

        return teacher


class PossibleTeacherPositionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = PossibleTeacherPosition
        fields = ('id', 'name', 'date_created', 'date_modified',)


class AdminSerializer(BaseSerializer):
    user = UserSerializer(many=False)


    class Meta:
        model = Admin
        fields = ('user',)


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        admin = Admin.objects.create(**validated_data)
        User.objects.create(**user_data, user_type='admin')

        return admin
