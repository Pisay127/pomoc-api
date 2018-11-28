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
        fields = ('user', 'year_level',)


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data, user_type='student')
        student = Student.objects.create(**validated_data, user=user)

        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.year_level = validated_data.get('year_level',
                                                 instance.year_level)
        instance.save()

        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('username', user.first_name)
        user.middle_name = validated_data.get('username', user.middle_name)
        user.last_name = validated_data.get('username', user.last_name)
        user.birth_date = validated_data.get('birth_date', user.birth_date)
        user.email = validated_data.get('email', user.email)
        user.avatar = validated_data.get('avatar', user.avatar)
        user.save()

        return instance


class StudentStatusSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentStatus
        fields = ('id',
                  'student_id',
                  'status',
                  'quarter',
                  'year_level',
                  'school_year',)


class StudentMonthlyAttendanceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentMonthlyAttendance
        fields = ('id',
                  'student_id',
                  'monthly_required_days_id',
                  'quarter',
                  'year_level',
                  'days_present',
                  'days_tardy',
                  'days_absent',)


class StudentSectionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentSection
        fields = ('id',
                  'student_id',
                  'section_id',
                  'school_year',)


class StudentRatingSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentRating
        fields = ('id',
                  'student_id',
                  'criterion_id',
                  'rating',
                  'quarter',
                  'year_level',
                  'school_year',)


class StudentBatchSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = StudentBatch
        fields = ('id', 'student_id', 'batch_id',)


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
        user = User.objects.create(**user_data, user_type='teacher')
        teacher = Teacher.objects.create(**validated_data, user=user)

        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('username', user.first_name)
        user.middle_name = validated_data.get('username', user.middle_name)
        user.last_name = validated_data.get('username', user.last_name)
        user.birth_date = validated_data.get('birth_date', user.birth_date)
        user.email = validated_data.get('email', user.email)
        user.avatar = validated_data.get('avatar', user.avatar)
        user.save()

        return instance


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
        user = User.objects.create(**user_data, user_type='admin')
        admin = Admin.objects.create(**validated_data, user=user)

        return admin

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('username', user.first_name)
        user.middle_name = validated_data.get('username', user.middle_name)
        user.last_name = validated_data.get('username', user.last_name)
        user.birth_date = validated_data.get('birth_date', user.birth_date)
        user.email = validated_data.get('email', user.email)
        user.avatar = validated_data.get('avatar', user.avatar)
        user.save()

        return instance
