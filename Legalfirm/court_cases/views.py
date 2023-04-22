from django.shortcuts import render, redirect
from menu.forms import JudgmentForm
from menu.models import Judgment
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Case

def add_judgment(request):
    if request.method == 'POST':
        form = JudgmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judgment_list')
    else:
        form = JudgmentForm()
    return render(request, 'add_judgment.html', {'form': form})

def judgment_list(request):
    judgments = Judgment.objects.all()
    return render(request, 'judgment_list.html', {'judgments': judgments})


class CaseUpdateView(UpdateView):
    model = Case
    fields = ['name', 'court', 'date', 'description']
    template_name_suffix = '_update_form'

class CaseDeleteView(DeleteView):
    model = Case
    success_url = reverse_lazy('cases-list')