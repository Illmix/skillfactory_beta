from django.shortcuts import render
from django.views.generic import ListView  # импортируем уже знакомый generic
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from .models import Product
from .filters import ProductFilter  # импортируем недавно написанный фильтр
from .forms import ProductForm  # импортируем нашу форму


# Create your views here.

class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    form_class = ProductForm

    def get_context_data(self,
                         **kwargs):  # забираем отфильтрованные объекты переопределяя метод
        # get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фиьтр в контекст
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)
