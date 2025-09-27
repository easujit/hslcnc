from django.urls import path
from . import views

urlpatterns = [
    path('permissions/', views.get_permissions),
    path('permissions/update/', views.update_permission),
    path('permissions/create/', views.create_permission),
    path('permissions/<int:policy_id>/delete/', views.delete_permission),
    path('menu-access/<str:menu_name>/', views.check_menu_access),
    path('user-permissions/', views.get_user_permissions),
    path('roles/', views.get_roles),
    path('metadata/', views.get_metadata),
    path('roles/<str:role_name>/permissions/', views.get_role_permissions),
]