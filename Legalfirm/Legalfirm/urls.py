"""
URL configuration for Legalfirm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from court_cases.views import CaseListView, CaseCreateView, CaseDetailView, CaseUpdateView, CaseDeleteView

urlpatterns = [
    path('', CaseListView.as_view(), name='cases-list'),
    path('create/', CaseCreateView.as_view(), name='case-create'),
    path('<int:pk>/', CaseDetailView.as_view(), name='case-detail'),
    path('<int:pk>/update/', CaseUpdateView.as_view(), name='case-update'),
    path('<int:pk>/delete/', CaseDeleteView.as_view(), name='case-delete'),
]