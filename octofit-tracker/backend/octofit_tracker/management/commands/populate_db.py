from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(name='Tony Stark', email='ironman@marvel.com', team='Marvel'),
            User(name='Steve Rogers', email='cap@marvel.com', team='Marvel'),
            User(name='Clark Kent', email='superman@dc.com', team='DC'),
            User(name='Bruce Wayne', email='batman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user_email='ironman@marvel.com', type='Running', duration=30, date='2026-01-01'),
            Activity(user_email='cap@marvel.com', type='Cycling', duration=45, date='2026-01-02'),
            Activity(user_email='superman@dc.com', type='Swimming', duration=60, date='2026-01-03'),
            Activity(user_email='batman@dc.com', type='Yoga', duration=20, date='2026-01-04'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel'),
            Workout(name='Power Yoga', description='Yoga for super strength', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
