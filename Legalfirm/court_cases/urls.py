from django.urls import path
from .views import CaseListView, CaseDetailView, CaseCreateView, CaseUpdateView, CaseDeleteView

app_name = 'court_cases'

urlpatterns = [
    path('', CaseListView.as_view(), name='case_list'),
    path('<int:pk>/', CaseDetailView.as_view(), name='case_detail'),
    path('create/', CaseCreateView.as_view(), name='case_create'),
    path('<int:pk>/update/', CaseUpdateView.as_view(), name='case_update'),
    path('<int:pk>/delete/', CaseDeleteView.as_view(), name='case_delete'),
]
