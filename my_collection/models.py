from django.db import models
from django.urls import reverse


# объявим новый класс, который будет описывать менеджер для моделей, следующим образом:
class PublishedModel(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_published=1)


# объявляем метод get_queryset(), который вызывается для получения списка
# записей из таблиц БД с помощью этого менеджера

class Goda(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True)  # параметр db_index указывает СУБД

	# индексировать данное поле, чтобы поиск по нему происходил быстрее.

	def __str__(self):
		return self.name


# Create your models here.
class My_collection(models.Model):
	SERIA_CHOICES = [
		('Cпорт', 'Cпорт'),
		('Cвязь', 'Cвязь'),
		('Фауна', 'Фауна'),
		('Флора', 'Флора'),
		('Стандарт', 'Стандарт'),
		('Военная', 'Военная'),
		('История', 'История'),
		('Культура', 'Культура'),
		('Техника', 'Техника'),
		('Космос', 'Космос'),
		('Заповедники', 'Заповедники'),
		('География', 'География'),

	]

	# blank=True. Данный параметр означает, что это поле может быть пустым, то есть, не содержать текста

	year = models.IntegerField(null=True, blank=True, verbose_name='Год')
	slug = models.SlugField(max_length=255, db_index=True, unique=True)
	nomer = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер')
	nomer_dliy_otobrajeniy = models.CharField(max_length=30, null=True, blank=True,
											  verbose_name='Номер порядковый для сайта')
	# izobrajenie = models.ImageField(upload_to='images/', max_length=100, default='', blank=True,
	#                                 verbose_name='Изображение')
	nominal = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номинал')
	rubrika = models.CharField(max_length=200, null=True, blank=True, verbose_name='Рубрика')
	name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название')
	opisanie = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание')

	seria = models.CharField(max_length=200, null=True, blank=True, choices=SERIA_CHOICES, default='',
							 verbose_name='Серия')  # добавление элементов выбора
	pod_seria = models.CharField(max_length=200, null=True, blank=True, default='', verbose_name='Подсерия')
	blok = models.CharField(max_length=200, null=True, blank=True, verbose_name='Блок/Номер')
	pechat = models.CharField(max_length=200, null=True, blank=True, verbose_name='Печать')
	bumaga = models.CharField(max_length=200, null=True, blank=True, verbose_name='Бумага')
	perforaciy = models.CharField(max_length=200, null=True, blank=True, verbose_name='Перфорация')
	cena_chist_katalog = models.CharField(max_length=30, null=True, blank=True,
										  verbose_name='Цена чистая каталог (Загорский')
	cena_chist_meshoc = models.CharField(max_length=30, null=True, blank=True, verbose_name='Цена чистой (Мешок')
	razmer = models.CharField(max_length=30, null=True, blank=True, verbose_name='Размер')
	tiraj = models.IntegerField(null=True, blank=True, verbose_name='Тираж')
	nalichie = models.CharField(max_length=150, null=True, blank=True, verbose_name='Наличие марки/блока')
	listu = models.CharField(max_length=150, null=True, blank=True, verbose_name='Наличие листов')
	malue_listu = models.CharField(max_length=150, null=True, blank=True, verbose_name='Наличие малых листов')
	raznovidnost = models.CharField(max_length=150, null=True, blank=True, verbose_name='Наличие разновидности')
	suvenirnuy_nabor_oblojki = models.CharField(max_length=150, null=True, blank=True,
												verbose_name='Наличие сувенирного набора')
	marochnuy_buklet = models.CharField(max_length=150, null=True, blank=True, verbose_name='Наличие марочного буклета')
	podarochnuy_nabor = models.CharField(max_length=150, null=True, blank=True,
										 verbose_name='Наличие подарочного набора')
	goda = models.ForeignKey(Goda, blank=True, null=True, on_delete=models.PROTECT,
							 related_name='blog_posts')  # суффикс _id для формирования поля cat_id Django добавит автоматически

	# class Meta:
	# 	verbose_name = 'Моя коллекция'
	# 	verbose_name_plural = 'Моя коллекция'
	# 	ordering = ['']
	# 	indexes = [
	# 		models.Index(fields=['']),
	# 	]

	objects = models.Manager()  # чтобы работал менеджер objects
	published = PublishedModel()

	def __str__(self):  # выводить заголовок – поле title.
		# Для этого в модели достаточно переопределить
		# магический метод __str__:
		return self.name

	def get_absolute_url(self):
		return reverse('marki_concretn', kwargs={'marki_concretn_slug': self.slug})

# формировать нужный нам URL-адрес по параметру slug с помощью метода get_absolute_url()

# class Goda(models.Model):
# 	name = models.CharField(max_length=100, db_index=True)
# 	slug = models.SlugField(max_length=255, unique=True, db_index=True)		# параметр db_index указывает СУБД
# 	# индексировать данное поле, чтобы поиск по нему происходил быстрее.
#
# 	def __str__(self):
# 		return self.name


# Команду makemigrations следует выполнять каждый раз, когда у нас меняется хотя бы одна модель
#  Итак, для выполнения миграций запишем команду:
# python manage.py migrate
