# Generated by Django 2.1.3 on 2018-11-28 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181128_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Batch')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentMonthlyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('quarter', models.PositiveSmallIntegerField(verbose_name='Quarter')),
                ('year_level', models.PositiveSmallIntegerField(verbose_name='Year Level')),
                ('days_present', models.PositiveSmallIntegerField(verbose_name='Days Present')),
                ('days_tardy', models.PositiveSmallIntegerField(verbose_name='Days Tardy')),
                ('days_absent', models.PositiveSmallIntegerField(verbose_name='Days Absent')),
                ('monthly_required_days_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.StudentMonthlyRequiredDays')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('rating', models.CharField(max_length=1, verbose_name='Rating')),
                ('quarter', models.PositiveSmallIntegerField(verbose_name='Quarter')),
                ('year_level', models.PositiveSmallIntegerField(verbose_name='Year Level')),
                ('school_year', models.TextField(verbose_name='School Year')),
                ('criterion_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.StudentCharacterRatingCriteria')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('school_year', models.TextField(verbose_name='School Year')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Section')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='studentstatus',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student'),
        ),
    ]
