from django.http import HttpResponse
from .models import Character, Fighter, Mage, Cleric, Thief
from django.shortcuts import render

def index(request):
    return HttpResponse("Character Creator App!!!")
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)
def view_character(request):
    return HttpResponse("hello")