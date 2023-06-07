from django.shortcuts import render, redirect
from .models import ServiceModels, TaskModels, SolutionModels, UserModels


# Create your views here.
def main(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(surname, name, phone, email)
        if surname and name and phone and email:
            UserModels.objects.create(surname=surname, name=name, phone=phone, email=email)
            return redirect('atom:main')
        else:
            return redirect('atom:main')
    return render(request, 'main.html')


def service(request):
    object = ServiceModels.objects.all()
    print(object)
    context = []
    for i in range(len(object)):
        context.append(object.values('description', 'name', 'cost', 'image')[i])

    return render(request, 'service.html', {'context': context})


def topic(request):
    return render(request, 'topic.html')


def task(request):
    if request.method == 'GET':
        task = TaskModels.objects.first()  # Получаем первую задачу из базы данных (вам нужно настроить логику выбора задачи)
        return render(request, 'task.html', {'task': task})
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        solution = SolutionModels(name=name, email=email, description=description)
        solution.save()
        return redirect('atom:task')
