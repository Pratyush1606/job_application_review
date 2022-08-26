from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import JsonResponse
from django.shortcuts import render, redirect

from review_application.models import Candidate, CandidateAcademic, CandidateProfessionalExp
from review_application.serializers import CandidateSerializer, CandidateAcademicSerializer, CandidateProfessionalExpSerializer


class CandidateList(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        candidates = Candidate.objects.all()
        candidates_serilaizers = CandidateSerializer(candidates, many=True)
        return Response(data={"candidates": candidates_serilaizers.data},
                        template_name="homepage.html",
                        status=status.HTTP_200_OK)


class AddPersonalDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name="personal_detail.html",
                        status=status.HTTP_200_OK)

    def post(self, request):
        details = request.POST
        serializer = CandidateSerializer(data=details)
        if (serializer.is_valid()):
            serializer.save()
            return redirect("review_application:acad",
                            candidate_id=serializer.data["candidate_id"])
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AddAcademicDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, candidate_id):

        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        candidate_details = CandidateSerializer(candidate).data
        return Response(data={"candidate": candidate_details},
                        template_name="academic_detail.html",
                        status=status.HTTP_200_OK)

    def post(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        candidate_details = CandidateSerializer(candidate).data
        details = request.POST.copy()
        details["candidate_id"] = candidate_id
        serializer = CandidateAcademicSerializer(data=details)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"candidate": candidate_details},
                            template_name="academic_detail.html",
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AddProfessionalDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        candidate_details = CandidateSerializer(candidate).data
        return Response({"candidate": candidate_details},
                        template_name="professional_detail.html",
                        status=status.HTTP_200_OK)

    def post(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        candidate_details = CandidateSerializer(candidate).data
        details = request.POST.copy()
        details["candidate_id"] = candidate_id
        serializer = CandidateProfessionalExpSerializer(data=details)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"candidate": candidate_details},
                            template_name="professional_detail.html",
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CandidateDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Getting Personal Detail
        personal_detail = CandidateSerializer(candidate).data

        # Getting Academic Details
        academics = CandidateAcademic.objects.filter(candidate_id=candidate_id)
        academic_detail = CandidateAcademicSerializer(academics, many=True).data

        # Getting Professional Details
        prof_exps = CandidateProfessionalExp.objects.filter(
            candidate_id=candidate_id)
        prof_detail = CandidateProfessionalExpSerializer(prof_exps,
                                                         many=True).data

        return Response(data={
            "personal": personal_detail,
            "academic": academic_detail,
            "professional": prof_detail
        },
                        template_name="candidate_detail.html",
                        status=status.HTTP_200_OK)


class Reject(APIView):

    def post(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        candidate.status = "rejected"
        candidate.save()
        return Response(status=status.HTTP_200_OK)


class Accept(APIView):

    def post(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(candidate_id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        candidate.status = "accepted"
        candidate.save()
        return Response(status=status.HTTP_200_OK)
