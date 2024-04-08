from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
	path('', views.index, name='home'),
	path('about/', views.about, name='about'),
	path('addpage/', views.addpage, name='add_page'),
	path('contact/', views.contact, name='contact'),
	path('login/', views.login, name='login'),
	path('marki_all/', views.marki_all, name='marki_all'),
	path('stemps/', views.stemps, name='stemps'),
	path('marki_concretn/<slug:marki_concretn_slug>/', views.marki_concretn, name='marki_concretn'),
	# path('marki_concretn/<int:post_id>/', views.marki_concretn, name='marki_concretn'),
	path('category/<int:cat_id>/', views.show_category, name='category'),

]
