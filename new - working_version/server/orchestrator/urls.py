from django.urls import path
from . import views

urlpatterns = [
    path('process-now/', views.process_now),
    path('notifications/', views.notifications_list),
    path('tasks/', views.tasks_list),
]