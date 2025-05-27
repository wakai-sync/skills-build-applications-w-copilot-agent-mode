from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One")
        user2 = User.objects.create(email="user2@example.com", name="User Two")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1, user2])

        # Create test activities
        Activity.objects.create(type="Running", duration=30)
        Activity.objects.create(type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user="user1@example.com", score=100)
        Leaderboard.objects.create(user="user2@example.com", score=150)

        # Create test workouts
        Workout.objects.create(name="Morning Run", calories=300)
        Workout.objects.create(name="Evening Yoga", calories=200)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
