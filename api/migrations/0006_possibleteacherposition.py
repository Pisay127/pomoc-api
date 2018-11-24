# Generated by Django 2.1.3 on 2018-11-24 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_studentcharacterratingcriteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleTeacherPosition',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Base')),
                ('name', models.TextField(unique=True, verbose_name='Name')),
            ],
            bases=('api.base',),
        ),
    ]