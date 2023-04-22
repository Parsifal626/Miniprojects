from django.shortcuts import render, redirect
from .forms import JudgmentForm

def add_judgment(request):
    if request.method == 'POST':
        form = JudgmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judgment_list')
    else:
        form = JudgmentForm()
    return render(request, 'add_judgment.html', {'form': form})