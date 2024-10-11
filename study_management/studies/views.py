from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm

def delete_multiple_studies(request):
    if request.method == 'POST':
        study_ids = request.POST.getlist('study_ids')
        if study_ids:
            Study.objects.filter(id__in=study_ids).delete()
            return redirect('study_list')
    return redirect('study_list')

def study_list(request):
    studies = Study.objects.all()
    print(studies)
    return render(request, 'study_list.html', {'studies': studies})

def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
        return render(request, 'add_study.html', {'form': form})

def delete_study(request, pk):
    print(request)
    datatodelete = get_object_or_404(Study, pk=pk)
    if request.method == 'POST':
        datatodelete.delete()
        return redirect('study_list')
    return render(request, 'delete_study.html', {'study': datatodelete})

def edit_study(request, pk):
    editbyid = get_object_or_404(Study, id=pk)
    print(editbyid)

    if request.method == 'POST':
        form = StudyForm(request.POST, instance=editbyid)
        if form.is_valid():
            form.save()
            return redirect('study_list')  # Redirect to the study list or any other page
    else:
        form = StudyForm(instance=editbyid)

    return render(request, 'edit_study.html', {'form': form, 'study': editbyid})

def view_study(request, pk):
    study = get_object_or_404(Study, id=pk)
    return render(request, 'view_study.html', {'study': study})



    


# Create your views here.
