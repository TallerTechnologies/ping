from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    """a Player"""
    user = models.OneToOneField(User)


class Team(models.Model):
    """a Team, two players"""
    player_a = models.ForeignKey("Player", related_name="team_as_a")
    player_b = models.ForeignKey("Player", related_name="team_as_b")
    name = models.CharField(max_length=100, primary_key=True)
    matches_played = models.SmallIntegerField(default=0)
    matches_won = models.SmallIntegerField(default=0)
    matches_lost = models.SmallIntegerField(default=0)


class Match(models.Model):
    """a match"""
    team_a = models.ForeignKey("Team", related_name="match_as_a")
    team_b = models.ForeignKey("Team", related_name="match_as_b")
    winner = models.ForeignKey("Team", null=True, blank=True, related_name="match_won")
    date_start = models.DateTimeField(null=True, blank=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    played = models.NullBooleanField(default=False, null=True, blank=True)
    score_a = models.SmallIntegerField(default=0)
    score_b = models.SmallIntegerField(default=0)
    championship = models.ForeignKey("Championship")
    journey = models.ForeignKey("Journey")


class Championship(models.Model):
    """a Championship"""
    winner = models.ForeignKey("Team", null=True, blank=True, related_name="championship_won")
    date_start = models.DateTimeField(null=True, blank=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    date_registration_end = models.DateTimeField(null=True, blank=True)
    registration_allowed = models.BooleanField(default=True)

class Journey(models.Model):
    """a day of matches"""
    championship = models.ForeignKey("Championship")
    date = models.DateField(null=True, blank=True)
