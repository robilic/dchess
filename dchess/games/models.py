from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    turn = models.IntegerField(null=False, blank=False, default=1)
    move = models.IntegerField(null=False, blank=False, default=1)
    white = models.ForeignKey(User, related_name='white', on_delete=models.DO_NOTHING, null=True, blank=True)
    black = models.ForeignKey(User, related_name='black', on_delete=models.DO_NOTHING, null=True, blank=True)
    winner = models.ForeignKey(User, related_name='winner', on_delete=models.DO_NOTHING, null=True, blank=True)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.DO_NOTHING, null=True, blank=True)
    challenger = models.ForeignKey(User, related_name='challenger', on_delete=models.DO_NOTHING, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    board = models.CharField(max_length=64, default='rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR')
    description = models.CharField(max_length=64)
    castlestatus_w = models.CharField(max_length=8, default='both')
    castlestatus_b = models.CharField(max_length=8, default='both')

    def turn_color(self):
    	if self.turn == 1:
    		return 'white'
    	elif self.turn == 0:
    		return 'black'
    	else:
    		return 'turn_color() error'

class MoveHistory(models.Model):
    game = models.ForeignKey(Game, related_name='game', on_delete=models.DO_NOTHING, null=False, blank=True)
    move = models.IntegerField(null=False, blank=False)
    black = models.CharField(max_length=6)
    white = models.CharField(max_length=6)
