from django.core.management import BaseCommand, call_command
from recorder.models.core import RecordedUser
# from yourapp.models import User # if you have a custom user


class Command(BaseCommand):
    help = "DEV COMMAND: Fill databasse with a set of data for testing purposes"

    def handle(self, *args, **options):
        call_command('loaddata','initial_user_data')
        # Fix the passwords of fixtures
        for user in RecordedUser.objects.all():
            user.set_password(user.password)
            user.save()
        call_command('loaddata','initial_data')