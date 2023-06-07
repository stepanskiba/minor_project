from django.shortcuts import render, redirect
from .models import ServiceModels, TaskModels, SolutionModels
from .models import ScheduleTopicModels, UserModels

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

    timetable_data = []

    # Получаем все объекты TimetableModels из базы данных
    timetables = ScheduleTopicModels.objects.all()

    # Создаем словарь, который будет хранить данные расписания для каждого временного слота
    schedule_data = {}

    # Заполняем словарь schedule_data данными из модели TimetableModels
    for timetable in timetables:
        date = timetable.date
        level = timetable.level
        title = timetable.title

        if date not in schedule_data:
            schedule_data[date] = {}

        schedule_data[date][level] = {'title': title}

    # Получаем список временных слотов, отсортированных по времени
    dates = sorted(schedule_data.keys())

    # Получаем список дней недели
    levels = ['1', '2', '3', '4']

    # Создаем список словарей timetable_data для отображения в шаблоне
    for date in dates:
        row_data = {'date': date}

        for level in levels:
            title = schedule_data.get(date, {}).get(level)
            row_data[level.lower() + '_title'] = title

        timetable_data.append(row_data)
    print(timetable_data)
    context = {'timetable_data': timetable_data}
    return render(request, 'topic.html', context)

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
