from django.http import HttpResponse
from .models import Character, Fighter, Mage, Cleric, Thief
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def index(request):
    return HttpResponse("Character Creator App!!!")

@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)
def view_character(request):
    return HttpResponse("hello")