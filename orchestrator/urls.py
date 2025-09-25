
from django.urls import path
from .views import list_notifications, list_tasks, process_now
urlpatterns = [
    path('notifications/', list_notifications),
    path('tasks/', list_tasks),
    path('process-now/', process_now),
]
