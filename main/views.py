from django.shortcuts import render, redirect
from .models import Test
from .forms import TestForm
text = "Нечеткая логика – это логическая или управляющая система n-значной логической системы, которая использует степени состояния («степени правды») входов и формирует выходы, зависящие от состояний входов и скорости изменения этих состояний. Это не обычная «истинная или ложная» (1 или 0), булева (двоичная) логика, на которой основаны современные компьютеры. Она в основном обеспечивает основы для приблизительного рассуждения с использованием неточных решений и позволяет использовать лингвистические переменные. В выбранной системе по диагностике тахикардии нечёткая логика помогает определять, насколько вероятна болезнь у человека. Самым удобным способом реализации оказалась Python разработка с использованием модуля PyQt5."


def index(request):
    test = Test.objects.all()
    return render(request, 'main/index.html', {'tests': test})


def fazi(request):
    return render(request, 'main/fazi.html')


def agregator(request):
    return render(request, 'main/agregator.html')


def defazi(request):
    return render(request, 'main/defazi.html')


def interface(request):
    return render(request, 'main/interface.html')


def test(request):
    return render(request, 'main/test.html')


def baza(request):
    return render(request, 'main/baza.html')


def prinad(request):
    return render(request, 'main/prinad.html')


def input(request):
    error = ""
    if request.method == 'POST':
        test = TestForm(request.POST)
        if test.is_valid():
            test.save()
            return render(request, 'main/test.html')
        else:
            error = "Вы заполнили что-то не так"

    form = TestForm()
    context = {
        'form': form,
        'error': error,

    }
    return render(request, 'main/input.html', context)


def btn1(request):
    return render(request, 'main/test.html')
