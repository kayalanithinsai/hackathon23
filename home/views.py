from django.http import HttpResponse
from django.shortcuts import render
import re
from .models import InputTable
from .models import FeedbackDatabase

def save_to_feedback_database(exception, solution=''):
    feedback = FeedbackDatabase(
        exception=exception,
        solution=solution
    )
    feedback.save()


def save_to_input_table(exception, cluster, step, date=None, time_taken=None, exception_label=''):
    input_table = InputTable(
        date=date,
        exception=exception,
        cluster=cluster,
        step=step,
        time_taken=time_taken,
        exception_label=exception_label
    )
    input_table.save()

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'response': '', 'hide_upload' : True, 'show_notification': False})
    elif request.method == 'POST':
        selected_values = list(request.POST.getlist('checkbox'))
        exception = request.POST.get('exception')
        otherInp = request.POST.get('otherInput')
        if 'others' in selected_values:
            selected_values.remove('others')
            selected_values.append(otherInp)
        for i in range(len(selected_values)):
            save_to_feedback_database(exception, selected_values[i])
        return render(request, 'index.html', {'response': '', 'hide_upload': True, 'show_notification': True})

def f(error_lines):
    respose = ['Solution 1','Solution 2', 'Solution 3', 'Solution 4', 'Solution 5']
    return respose


def handle_uploaded_file(file):
    decoded_lines = [line.decode('utf-8') for line in file]
    error_lines = [line for line in decoded_lines if re.search(r'Error', line, re.IGNORECASE)]
    return error_lines


def solutions(request):
    if request.method == 'POST':
        file = request.FILES['file']
        cluster = request.POST['clusterType']
        step = request.POST['stepType']
        error_lines = handle_uploaded_file(file) # file needs to be filtered.
        list_of_solutions = f(error_lines) # ML code is called.
        save_to_input_table(error_lines[0], cluster, step)
        return render(request, 'solutions.html', {'exception': str(error_lines), 'data': list_of_solutions})

    else:
        data = [{'solution': 'Solution 1'}, {'solution': 'Solution '}]
        return render(request, 'solutions.html', {'data': data})

