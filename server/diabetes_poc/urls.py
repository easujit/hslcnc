from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/config/", include("configurator.urls")),
    path("api/runtime/", include("runtime_engine.urls")),
    path("api/submit/", include("submission.urls")),
    path("api/clinical/", include("clinical.urls")),
    path("api/orchestrator/", include("orchestrator.urls")),
    path("api/ext/", include("extensions.urls")),
    path("api/policies/", include("policies.urls")),
    path("api/consent/", include("consent.urls")),
]