from django.http import HttpResponse
from django.shortcuts import render
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def get_cont(request, a):
    servings = int(request.GET.get('servings', 1))
    new_data = copy.deepcopy(DATA)
    if servings != 1:
        for k in new_data:
            for i, v in new_data[k].items():
                new_data[k][i] = v * servings
    if a == 'omlet':
        context = {'recipe': new_data['omlet']}
    elif a == 'pasta':
        context = {'recipe': new_data['pasta']}
    elif a == 'buter':
        context = {'recipe': new_data['buter']}
    else:
        context = {}
    return render(request, 'calculator/index.html', context)
    # return HttpResponse(context)
