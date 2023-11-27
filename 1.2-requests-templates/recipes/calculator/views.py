from django.shortcuts import render

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


def index(request):
    context = {'recipe': DATA}
    return render(request, 'calculator/index.html', context)


def recipes(request, dish):
    qty = int(request.GET.get('servings', '1'))
    recipe = DATA.get(dish)
    if recipe:
        context = {'recipe': {i[0]: round(i[1] * qty, 3) for i in recipe.items()}}
    else:
        context = {}
    return render(request, 'calculator/index.html', context)
