from django.shortcuts import render, get_object_or_404
from .models import PersonalInformation, Project

# Create your views here.
def home(request):
    personal = PersonalInformation.objects.first()
    projects = Project.objects.all()
    
    return render(
        request,
        "main/index.html",
        {
            "personal": personal,
            "projects": projects,
        }
    )

def project_list(request):

    projects = Project.objects.all()

    return render(
        request,
        "main/project_list.html",
        {
            "projects": projects,
        }
    )

def project_detail(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    return render(
        request,
        "main/project_detail.html",
        {
            "project": project,
        }
    )