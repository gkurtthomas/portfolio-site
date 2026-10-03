from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import PersonalInformation, Project, Testimony, TechStack
from .forms import ProjectForm, InquiryForm, TestimonyForm, TechStackForm
from django.views.generic import ListView

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

@user_passes_test(lambda user: user.is_superuser, login_url="signin")
def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    else:

        form = ProjectForm()

    return render(
        request,
        "main/add_project.html",
        {"form": form},
    )

def add_inquiry(request):

    if request.method == "POST":

        form = InquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = InquiryForm()

    return render(
        request,
        "main/add_inquiry.html",
        {"form": form},
    )

def add_testimony(request):

    if request.method == "POST":

        form = TestimonyForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("testimony_list")

    else:

        form = TestimonyForm()

    return render(
        request,
        "main/add_testimony.html",
        {"form": form},
    )

class TestimonyListView(ListView):
    model = Testimony
    template_name = "main/testimony_list.html"
    context_object_name = "testimonies"

def testimony_detail(request, testimony_id):

    testimony = get_object_or_404(
        Testimony,
        id=testimony_id
    )

    return render(
        request,
        "main/testimony_detail.html",
        {
            "testimony": testimony,
        }
    )

def signin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("dashboard")

        messages.error(request, "You do not have permission to access the dashboard.")
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "main/signin.html")


@user_passes_test(lambda user: user.is_superuser, login_url="signin")
def dashboard(request):
    projects = Project.objects.prefetch_related("tech_stack").all()
    tech_stacks = TechStack.objects.prefetch_related("project_set").all()

    return render(request, "main/dashboard.html", {
        "projects": projects,
        "tech_stacks": tech_stacks,
    })

def signout(request):
    logout(request)
    return redirect("signin")

@user_passes_test(lambda user: user.is_superuser, login_url="signin")
def add_tech_stack(request):
    if request.method == "POST":
        form = TechStackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = TechStackForm()

    return render(request, "main/add_tech_stack.html", {
        "form": form
    })