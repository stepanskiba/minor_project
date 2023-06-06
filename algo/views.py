from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import CreateAbcForm
from .models import SumMoney
from math import pi


def form_send(request):
    # print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            # print("\nform_is_valid:\n", form)
            form.save()
            return redirect('algo:form_result')
    else:
        form = CreateAbcForm()
        # print('\nform_else:\n', form)
    context = {'form': form}
    #  print("\ncontext:\n", context)
    return render(request, 'form_send.html', context)

def form_result(request):
    object = SumMoney.objects.all().order_by('-id')[:1]
    print("object: ", object)
    # dict
    row = object.values('S')[0]
    print("row: ", row)
    # list
    row_list = object.values_list()[0]
    print("row_list: ", row_list)


    # Проверяем, можно ли разменять сумму

    # Инициализируем переменные для хранения количества купюр и монет разного номинала
    num_500 = num_100 = num_10 = num_2 = 0

    # Разменяем сумму начиная с крупных купюр
    while row['S'] >= 500:
        row['S'] -= 500
        num_500 += 1

    while row['S'] >= 100:
        row['S'] -= 100
        num_100 += 1

    while row['S'] >= 10:
        row['S'] -= 10
        num_10 += 1

    while row['S'] >= 2:
        row['S'] -= 2
        num_2 += 1

    # Формируем строку с результатом
    result = f"500 руб. купюр: {num_500} "
    result += f"100 руб. купюр: {num_100} "
    result += f"10 руб. купюр: {num_10} "
    result += f"2 руб. монет: {num_2}"

    if row['S'] % 2 != 0:
        result = "Невозможно разменять данную сумму."

    task = row_list[1]
    print('task: ', task)
    last_data = [row_list[2]]
    print('last_data:', last_data)
    print('result: ', result)
    context = {'task': task, 'last_data': last_data, 'result': result, 'row': row}
    return render(request, 'form_result.html', context)


def table(request):
    row = SumMoney.objects.values()
    print('row:', row)
    row_lists = SumMoney.objects.values_list()
    print('row_lists:', row_lists)
    cur_objects = SumMoney.objects.all()
    statics_val = [cur_objects.aggregate(Count('S')), cur_objects.aggregate(Avg('S')), cur_objects.aggregate(Min('S')),
                   cur_objects.aggregate(Max('S')), cur_objects.aggregate(StdDev('S')), cur_objects.aggregate(Sum('S'))]
    print(statics_val)
    statics = {'statics_val': statics_val}

    fields = SumMoney._meta.get_fields()
    print(fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print(verbose_name_list)
    print(name_list)
    field_names = verbose_name_list
    context = {'row': row, 'row_lists': row_lists, 'field_names': field_names, 'statics': statics}
    return render(request, 'table.html', context)
