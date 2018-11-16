from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Project
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects=Project.get_projects()
    return render(request,'index.html',{"projects":projects})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
