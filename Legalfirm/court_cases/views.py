from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Case

class CaseListView(ListView):
    model = Case
    template_name = 'court_cases/case_list.html'
    context_object_name = 'cases'
    

class CaseDetailView(DetailView):
    model = Case
    template_name = 'court_cases/case_detail.html'
    context_object_name = 'case'

class CaseCreateView(CreateView):
    model = Case
    template_name = 'court_cases/case_form.html'
    fields = '__all__'

class CaseUpdateView(UpdateView):
    model = Case
    template_name = 'court_cases/case_form.html'
    fields = '__all__'

class CaseDeleteView(DeleteView):
    model = Case
    template_name = 'court_cases/case_confirm_delete.html'
    success_url = reverse_lazy('case_list')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        results = Case.objects.filter(title__icontains=query)
        return render(request, 'court_cases/search_results.html', {'results': results})
