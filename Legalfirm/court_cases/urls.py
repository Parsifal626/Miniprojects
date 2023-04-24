from django.urls import path
from .views import CaseListView, CaseDetailView, CaseCreateView, CaseUpdateView, CaseDeleteView, search

urlpatterns = [
    path('case/new/', CaseCreateView.as_view(), name='case_new'),
    path('', CaseListView.as_view(), name='case_list'),
    path('case/<int:pk>/', CaseDetailView.as_view(), name='case_detail'),
    path('case/new/', CaseCreateView.as_view(), name='case_form'),
    path('case/<int:pk>/edit/', CaseUpdateView.as_view(), name='case_update'),
    path('case/<int:pk>/delete/', CaseDeleteView.as_view(), name='case_delete'),
    path('search/', search, name='search'),
]
