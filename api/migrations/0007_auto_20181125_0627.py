# Generated by Django 2.1.3 on 2018-11-25 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_possibleteacherposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMonthlyRequiredDays',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Base')),
                ('month', models.PositiveSmallIntegerField(verbose_name='Month')),
                ('school_year', models.TextField(verbose_name='School Year')),
                ('num_days', models.PositiveSmallIntegerField(blank=True, verbose_name='Required Number of Days')),
            ],
            bases=('api.base',),
        ),
        migrations.AlterUniqueTogether(
            name='studentmonthlyrequireddays',
            unique_together={('month', 'school_year')},
        ),
    ]
