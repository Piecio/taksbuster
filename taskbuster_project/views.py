from django.shortcuts import render


def home(request):
    return render(request, "taskbuster_project/index.html", {})