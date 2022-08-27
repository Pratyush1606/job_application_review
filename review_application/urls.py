from django.urls import path, include
from review_application import views

app_name = "review_application"
urlpatterns = [
    path("", views.CandidateList.as_view(), name="homepage"),
    path("pers_detail", views.AddPersonalDetail.as_view(), name="pers_detail"),
    path(
        "prof_exp/<int:candidate_id>",
        views.AddProfessionalDetail.as_view(),
        name="prof_exp",
    ),
    path("acad/<int:candidate_id>", views.AddAcademicDetail.as_view(), name="acad"),
    path(
        "cand_detail/<int:candidate_id>",
        views.CandidateDetail.as_view(),
        name="cand_detail",
    ),
    path("accept/<int:candidate_id>", views.Accept.as_view(), name="accept"),
    path("reject/<int:candidate_id>", views.Reject.as_view(), name="reject"),
]
