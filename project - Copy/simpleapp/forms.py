from django.forms import ModelForm, BooleanField
from .models import Product


# Создаём модельную форму
class ProductForm(ModelForm):
    # в класс мета, как обычно,
    # надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с
    # фильтрами.
    check_box = BooleanField(label='Confirm!')

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'check_box']
