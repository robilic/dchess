from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import games.chessUtils as cu
import copy
import sys

from .models import Game
from .forms import Create

# Create your views here.

def index(request):
	games_list = Game.objects.all()
	context = { 'games_list': games_list }
	return render(request, 'games/index.html', context)

def detail(request, game_id):
	game = Game.objects.get(pk=game_id)
	context = { 'game': game }
	return render(request, 'games/detail.html', context)

def new(request):
	form = Create()
	game_instance = Game()
	context = { 'form': form, 'game_instance': game_instance, }

	return render(request, 'games/new.html', context)

def create(request):
	context = {}
	return render(request, 'games/new.html', context)

def game(request, game_id):
	game = Game.objects.get(pk=game_id)
	board = cu.readBoardDB(game_id)
	output = cu.boardHTML(board)
	context = { 'game': game, 'output': output, 'game_id': game_id }
	return render(request, 'games/game.html', context)

def move(request, game_id, movestring):
	print("Moving piece for " + request.user.username)
	print(" ID: " + str(request.user.id))

	game = Game.objects.get(pk=game_id)
	board = cu.readBoardDB(game_id)

	if board == 'NONE':
		return "INVALID GAME"

	print("game.turn_color = ", game.turn_color())
	print("request.user.id = ", request.user.id)
	print("g.black.id = ", game.black.id)
	print("g.white.id = ", game.white.id)

	if not cu.isPlayersTurn(request.user, game):
		print("Not your turn!")
		return redirect('games:game', game_id=game_id)

	# check the first peice to see if it's their peice
	x = cu.toArrayCoords(cu.toNumCoords(movestring[0]))
	y = cu.rankToArrayCoords(int(movestring[1]))
	print("Turn = ", game.turn, " and movestring[:2] is ", movestring[:2], " x,y = ", x, ", ", y)
	dx = cu.toArrayCoords(cu.toNumCoords(movestring[2]))
	dy = cu.rankToArrayCoords(int(movestring[3]))
	print("movestring[2:2] is", movestring[2:4], " x,y = ", dx, ", ", dy)
	print("Piece is ", board[y][x])

	if game.turn == 0: # black's turn
		if board[y][x].isupper():
			print("Not your piece")
			return redirect('games:game', game_id=game_id)
	elif game.turn == 1: # white's turn
		if board[y][x].islower():
			print("Not your piece")
			return redirect('games:game', game_id=game_id)
	else: # something isn't right
		print("Something weird happened")
		return redirect('games:game', game_id=game_id)
	
	result = cu.processMove(movestring, board)
	save_board = False
	if len(result) == 2:
		# wasn't a valid move
		print("INFO: " + result[0] + ', ' + result[1], file=sys.stderr)
	else:
		# we had a valid move
		board = result
		# check for self-check before saving
		# make a copy of the board becuase checkForCheck is destructive
		test_board = copy.deepcopy(board)
		if game.turn == 0: # black's turn
			if cu.checkForCheck('black', test_board):
				print("Can't put yourself in check")
			else:
				save_board = True
		elif game.turn == 1: # white's turn
			if cu.checkForCheck('white', test_board):
				print("Can't put yourself in check")
			else:
				save_board = True
		if save_board:
			game.turn = not game.turn # switch turns
			# increment move count
			# castle status
			game.save()
			cu.writeBoardDB(game_id, board)

	# re-direct
	return redirect('games:game', game_id=game_id)

