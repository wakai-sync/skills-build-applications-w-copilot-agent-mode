from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)

class Activity(models.Model):
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
