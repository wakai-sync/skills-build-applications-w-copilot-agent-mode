from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

# 他のモデルのテストも同様に追加
