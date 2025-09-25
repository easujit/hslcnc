
from django.urls import path
from .views import seed, effective_form, effective_rules, effective_workflow, publish_form, publish_rules, publish_workflow
urlpatterns = [
    path("seed/", seed),
    path("effective/form/<str:name>/", effective_form),
    path("effective/rules/<str:name>/", effective_rules),
    path("effective/workflow/<str:name>/", effective_workflow),
    path("publish/form/<str:name>/", publish_form),
    path("publish/rules/<str:name>/", publish_rules),
    path("publish/workflow/<str:name>/", publish_workflow),
]
