from rest_framework import serializers
from review_application.models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["candidate_id", "name", "email", "phone", "status"]


class CandidateAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateAcademic
        fields = [
            "candidate_id",
            "education",
            "degree",
            "major",
            "graduation_year",
            "gpa",
            "gpa_max",
        ]


class CandidateProfessionalExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfessionalExp
        fields = [
            "candidate_id",
            "company",
            "title",
            "start_date",
            "end_date",
            "currently_working",
            "description",
        ]
