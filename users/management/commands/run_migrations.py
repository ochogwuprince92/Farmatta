from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Runs migrations for the users app"

    def handle(self, *args, **kwargs):
        try:
            # Running migrations for the users app
            call_command('migrate', 'users')
            self.stdout.write(self.style.SUCCESS("Migrations applied successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))
