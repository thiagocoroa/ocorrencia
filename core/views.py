from django.shortcuts import render,redirect
from core.forms import NotificationForm, StudentForm
from django.views.generic.edit import FormView

# Create your views here.

def ocorrencia(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NotificationForm()
    return render(request, 'ocorrencia.html',{'form':form})

def aluno(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aluno')
    else:
        form = StudentForm()
    return render(request, 'aluno.html',{'form':form})
