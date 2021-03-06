# Generated by Django 2.1.3 on 2018-11-28 13:07

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_batchadvisor_sectionadvisor_subjectoffering_teacherposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSubjectGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('quarter', models.PositiveSmallIntegerField(verbose_name='Quarter')),
                ('grade', models.DecimalField(decimal_places=16, max_digits=17, validators=[django.core.validators.MinValueValidator(Decimal('1.0')), django.core.validators.MaxValueValidator(Decimal('5.0'))], verbose_name='Grade')),
                ('student_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.StudentSubject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSubjectPendingGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('proposed_grade', models.DecimalField(decimal_places=16, max_digits=17, verbose_name='Proposed Grade')),
                ('requesting_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Teacher')),
                ('student_subject_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.StudentSubjectGrade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='batchadvisor',
            old_name='advisor_id',
            new_name='advisor',
        ),
        migrations.RenameField(
            model_name='sectionadvisor',
            old_name='advisor_id',
            new_name='advisor',
        ),
        migrations.RenameField(
            model_name='sectionadvisor',
            old_name='section_id',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='subjectoffering',
            old_name='instructor_id',
            new_name='instructor',
        ),
        migrations.RenameField(
            model_name='subjectoffering',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='teacherposition',
            old_name='position_id',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='teacherposition',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.AddField(
            model_name='studentsubject',
            name='subject_offering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SubjectOffering'),
        ),
    ]
