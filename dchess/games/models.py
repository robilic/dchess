from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    turn = models.IntegerField(null=False, blank=False, default=1)
    white = models.ForeignKey(User, related_name='white', on_delete=models.DO_NOTHING, null=True, blank=True)
    black = models.ForeignKey(User, related_name='black', on_delete=models.DO_NOTHING, null=True, blank=True)
    winner = models.ForeignKey(User, related_name='winner', on_delete=models.DO_NOTHING, null=True, blank=True)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.DO_NOTHING, null=True, blank=True)
    challenger = models.ForeignKey(User, related_name='challenger', on_delete=models.DO_NOTHING, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    board = models.CharField(max_length=64)
    description = models.CharField(max_length=64)

    def turn_color(self):
    	if self.turn == 1:
    		return 'white'
    	elif self.turn == 0:
    		return 'black'
    	else:
    		return 'turn_color() error'
