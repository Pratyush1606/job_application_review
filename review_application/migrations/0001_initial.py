# Generated by Django 4.1 on 2022-08-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(default='applied', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfessionalExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('currently_working', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=250)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_prof_exp', to='review_application.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateAcademic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('graduation_year', models.IntegerField()),
                ('gpa', models.FloatField()),
                ('gpa_max', models.FloatField()),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_acad', to='review_application.candidate')),
            ],
        ),
    ]
