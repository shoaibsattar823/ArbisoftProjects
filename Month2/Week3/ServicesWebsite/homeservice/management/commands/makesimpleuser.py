from django.core.management.base import BaseCommand  # , CommandError
from django.contrib.auth.models import User
from django.utils.encoding import force_str
# from homeservice.models import Order
from getpass import getpass


class Command(BaseCommand):
    help = 'Closes the specified request for a service'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        # parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        if options['username']:
            username = options['username']
            email = options['email']
        password = None
        while password is None:
            password = getpass()
            if password == '':
                self.stderr.write("Error: Password should not be blank")
                password = None
                continue

            password2 = getpass(
                                force_str('Password (again): '))
            if password != password2:
                self.stderr.write(
                            "Error: Your passwords didn't match.")
                password = None
                # Don't validate passwords that don't match.
                continue

        User.objects.create_user(username=username,
                                 password=password,
                                 email=email)
        self.stdout.write(
                 self.style.SUCCESS(
                            'Successfully created user "%s"' % username
                 )
            )
