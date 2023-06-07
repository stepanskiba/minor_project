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
    timetables = TimetableModels.objects.all()

    # Создаем словарь, который будет хранить данные расписания для каждого временного слота
    schedule_data = {}

    # Заполняем словарь schedule_data данными из модели TimetableModels
    for timetable in timetables:
        time_slot = timetable.time_slot
        day = timetable.day
        instructor = timetable.instructor
        direction = timetable.direction

        if time_slot not in schedule_data:
            schedule_data[time_slot] = {}

        schedule_data[time_slot][day] = {'instructor': instructor, 'direction': direction}

    # Получаем список временных слотов, отсортированных по времени
    time_slots = sorted(schedule_data.keys())

    # Получаем список дней недели
    days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    # Создаем список словарей timetable_data для отображения в шаблоне
    for time_slot in time_slots:
        row_data = {'time_slot': time_slot}

        for day in days_of_week:
            instructor = schedule_data.get(time_slot, {}).get(day)
            row_data[day.lower() + '_instructor'] = instructor

        timetable_data.append(row_data)
    print(timetable_data)
    context = {'timetable_data': timetable_data}
    return render(request, 'timetable.html', context)

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
