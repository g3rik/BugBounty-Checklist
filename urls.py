from django.urls import path
from . import views

urlpatterns = [
   path('websites/', views.website_list, name='website_list'),
    path('websites/<int:website_id>/checklists/', views.checklist_detail, name='checklist_detail'),
    path('update_checklist_data/', views.update_checklist_data, name='checklist_list'),
    path('add_target/', views.add_target, name='add_target_page'),
]