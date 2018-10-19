from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'data': 'asdasd'}
    return render(request, 'frontend/index.html', context)
