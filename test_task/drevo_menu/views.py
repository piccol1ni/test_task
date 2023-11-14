from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'drevo_menu/index.html', context)
