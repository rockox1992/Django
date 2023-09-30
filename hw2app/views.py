from django.http import HttpResponse
from django.shortcuts import render


def show_hw_2(request):
    return HttpResponse(f"""<h2>HW 2</h2> <p><БАЗА ДАННЫХ></p>""")