from django.shortcuts import render
from boards.models import Board
import logging
# Create your views here.

def home(request):
	boards = Board.objects.all()
	print(boards)
	return render(request, 'index.html', {'boards': boards})
