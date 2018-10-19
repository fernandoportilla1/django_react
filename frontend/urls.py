from django.urls import path

from . import views

urlpatterns = [
	path('company', views.index, name='company-view' ),
    path('category', views.index, name='category-view' ),
]