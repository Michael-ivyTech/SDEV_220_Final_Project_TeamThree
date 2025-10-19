from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import VerificationToken
class Command(BaseCommand):
    help = 'Seed admin and two users'

    def handle(self, *args, **options):
        users = [
            ('admin','admin@example.com','AdminPass123!', True),
            ('alice','alice@example.com','AlicePass123!', False),
            ('bob','bob@example.com','BobPass123!', False),
        ]
        for username,email,password,is_staff in users:
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING(f'User {username} exists, skipping'))
                continue
            user = User.objects.create_user(username=username, email=email, password=password, is_staff=is_staff)
            user.save()
            # create verified token for admin and unverified for others
            token = VerificationToken.objects.create(user=user, token='seed-'+username, verified=is_staff)
            token.save()
            self.stdout.write(self.style.SUCCESS(f'Created user {username}'))
