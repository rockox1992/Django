from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_hw_2, name='hw_2'),  # по пустой строке у нас вызывется фу-ция index

]
