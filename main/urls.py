from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "projects/",
        views.project_list,
        name="project_list"
),

    path(
        "projects/<int:project_id>/",
        views.project_detail,
        name="project_detail"
),

    path(
    "projects/add/",
    views.add_project,
    name="add_project",
),

    path(
    "inquiry/add/",
    views.add_inquiry,
    name="add_inquiry"
),

    path(
    "testimonies/add/",
    views.add_testimony,
    name="add_testimony"
),

    path(
    "testimonies/",
    views.TestimonyListView.as_view(),
    name="testimony_list"
),

    path(
    "testimonies/<int:testimony_id>/",
    views.testimony_detail,
    name="testimony_detail"
),
]