
from django.urls import path
from .views import configurator_page, visit_page, home_page, visits_page, notifications_page, tasks_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('configurator/', configurator_page, name='configurator_page'),
    path('visit/', visit_page, name='visit_page'),
    path('visits/', visits_page, name='visits_page'),
    path('notifications/', notifications_page, name='notifications_page'),
    path('tasks/', tasks_page, name='tasks_page'),
]
