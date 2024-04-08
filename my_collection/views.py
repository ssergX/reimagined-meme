from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
# Create your views here.
from django.urls import reverse
from .models import My_collection

# class MyClass:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b


menu = [{'title': "О сайте", 'url_name': 'about'},
		{'title': "Добавить статью", 'url_name': 'add_page'},
		{'title': "Обратная связь", 'url_name': 'contact'},
		{'title': "Войти", 'url_name': 'login'}
		]

data_db = [
	{'id': 1, 'title': 'Марки', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], 
		при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); 
		род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, 
		телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, 
		посол доброй воли ООН. Обладательница премии «Оскар», трёх премий 
		«Золотой глобус» (первая актриса в истории, 
		три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».'''
	 },
	{'id': 2, 'title': 'Конверты', 'content': 'Конверты по годам'},
	{'id': 3, 'title': 'Открытки', 'content': 'Открытки по годам'},
	{'id': 4, 'title': 'Товары с дополненной реальностью', 'content': 'Товары'},
	{'id': 5, 'title': 'Филателистическая продукция', 'content': 'Филателистическая продукция'},
	{'id': 6, 'title': 'Сувенирная продукция', 'content': 'Сувенирная продукция'},
	{'id': 7, 'title': 'Периодические издания и каталоги', 'content': 'Периодические издания и каталоги'},
	{'id': 8, 'title': 'Штемпели', 'content': 'Штемпели'},
]

stemps_db = [
	{'id': 1, 'title': 'Марки', 'content': 'Марки по годам'},
	{'id': 2, 'title': 'Блоки', 'content': 'по годам'},
	{'id': 3, 'title': 'Малые листы', 'content': 'Открытки по годам'},
	{'id': 4, 'title': 'Листы', 'content': 'Товары'},
	{'id': 5, 'title': 'Разновидности', 'content': 'Филателистическая продукция'},
]

cats_db = [
	{'id': 1, 'name': '1991'},
	{'id': 2, 'name': '1992'},
	{'id': 3, 'name': '1993'},
]


def index(request):
	# posts = My_collection.objects.all()
	data = {
		'title': 'Главная страница',
		'menu': menu,
		'posts': data_db,

	}
	return render(request, 'my_collection/index.html', context=data)


def stemps(request):
	# stamps_db = My_collection.objects.all()
	stemps_all = {
		'title': 'Марки',
		'menu': menu,
		'stemps_db': stemps_db,

	}
	return render(request, 'my_collection/stemps.html', context=stemps_all)


def marki_all(request):
	# post = get_object_or_404(My_collection)
	post_marki = My_collection.objects.all()

	data = {
		'title': 'Марки',
		'menu': menu,
		'post_marki': post_marki,
	}
	return render(request, 'my_collection/marki_all.html', context=data)


# Давайте вначале сделаем отображение статей по их идентификатору, а затем, заменим адрес на слаг

# def marki_concretn(request, post_id):
# 	post_concretn = get_object_or_404(My_collection, pk=post_id)
def marki_concretn(request, marki_concretn_slug):
	post_concretn = get_object_or_404(My_collection, slug=marki_concretn_slug)

	data = {
		'title': post_concretn.name,
		'menu': menu,
		'post_concretn': post_concretn,
			}

	return render(request, 'my_collection/marki_concretn.html', context=data)

def show_category(request, cat_id):
	data = {
		'title': 'Отображение по рубрикам',
		'menu': menu,
		'posts': data_db,
		'cat_selected': cat_id,
	}
	return render(request, 'my_collection/index.html', context=data)


# def show_category(request, cat_id):
#     """Функция-заглушка"""
#     return index(request)

def addpage(request):
	return HttpResponse("Добавление статьи")


def contact(request):
	return HttpResponse("Обратная связь")


def login(request):
	return HttpResponse("Авторизация")


def about(request):
	return render(request, 'my_collection/about.html', {'title': 'О сайте', 'menu': menu})


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')
