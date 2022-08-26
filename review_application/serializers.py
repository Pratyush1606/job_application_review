from rest_framework import serializers
from review_application.models import *

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['candidate_id', 'name', 'email', 'phone', 'status']