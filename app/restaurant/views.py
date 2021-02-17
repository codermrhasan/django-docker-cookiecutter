from django.shortcuts import render
from .models import Food
from .forms import FoodForm


def home(request):
    template_name = 'restaurant/home.html'
    if request.method == "GET":
        foods = Food.objects.all()
        context = {
            'foods': foods,
            'form': FoodForm(),
        }
        return render(request, template_name, context=context)

    elif request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            
        foods = Food.objects.all()
        context = {
            'foods': foods,
            'form': FoodForm(),
        }
        return render(request, template_name, context=context)


