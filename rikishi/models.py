from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Rikishi(models.Model):
  
  class Rank(models.TextChoices):
    YOKOZUNA = 'Y', _('Yokozuna')
    OZEKI = 'O', _('Ōzeki')
    SEKIWAKE = 'S', _('Sekiwake')
    KOMUSUBI = 'K', _('Komusubi')
    MAEGASHIRA_1 = 'M1', _('Maegashira 1')
    MAEGASHIRA_2 = 'M2', _('Maegashira 2')
    MAEGASHIRA_3 = 'M3', _('Maegashira 3')
    MAEGASHIRA_4 = 'M4', _('Maegashira 4')
    MAEGASHIRA_5 = 'M5', _('Maegashira 5')
    MAEGASHIRA_6 = 'M6', _('Maegashira 6')
    MAEGASHIRA_7 = 'M7', _('Maegashira 7')
    MAEGASHIRA_8 = 'M8', _('Maegashira 8')
    MAEGASHIRA_9 = 'M9', _('Maegashira 9')
    MAEGASHIRA_10 = 'M10', _('Maegashira 10')
    MAEGASHIRA_11 = 'M11', _('Maegashira 11')
    MAEGASHIRA_12 = 'M12', _('Maegashira 12')
    MAEGASHIRA_13 = 'M13', _('Maegashira 13')
    MAEGASHIRA_14 = 'M14', _('Maegashira 14')
    MAEGASHIRA_15 = 'M15', _('Maegashira 15')
    MAEGASHIRA_16 = 'M16', _('Maegashira 16')
    MAEGASHIRA_17 = 'M17', _('Maegashira 17')
    MAEGASHIRA_18 = 'M18', _('Maegashira 18')
  
  shikona_first = models.CharField(max_length=50)
  shikona_last = models.CharField(max_length=50)
  highest_rank = models.CharField(
    max_length=3, 
    choices=Rank.choices,
    default=Rank.YOKOZUNA
  )
  total_wins = models.PositiveIntegerField()
  total_losses = models.PositiveIntegerField()
  total_absent = models.PositiveIntegerField()
  real_name_first = models.CharField(max_length=50)
  real_name_last = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  height = models.IntegerField(validators=[MinValueValidator(150), MaxValueValidator(250)])
  weight = models.DecimalField(max_digits=4, decimal_places=1)
  origin = models.CharField(max_length=100)
