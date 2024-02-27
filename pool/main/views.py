from django.shortcuts import render
from .models import AboutPool, Instructors, Schedule, WeekDay

def about(request):
    return render(request, 'main/about.html')


def index(request):
    pool_info = AboutPool.objects.all()
    instructors = Instructors.objects.all()

    data = {
        'pool_info': pool_info,
        'instructors': instructors
    }

    return render(request, 'main/index.html', data)

def schedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'main/schedule.html', {'schedule': schedule})

def instructors_view(request):
    instructors = Instructors.objects.all() # Получение всех инструкторов
    return render(request, 'main/instructors.html', {'instructors': instructors})

