
from django.shortcuts import render

def home_page(request):
    return render(request, "home.html", {})

def configurator_page(request):
    return render(request, "configurator.html", {})

def visit_page(request):
    return render(request, "visit.html", {})

def visits_page(request):
    return render(request, "visits.html", {})

def notifications_page(request):
    return render(request, "notifications.html", {})

def tasks_page(request):
    return render(request, "tasks.html", {})
