from django.core.management.base import BaseCommand, CommandError
from homeservice.models import Order


class Command(BaseCommand):
    help = 'Closes the specified request for a service'

    def add_arguments(self, parser):
        parser.add_argument('request_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for req_id in options['request_id']:
            try:
                request = Order.objects.get(pk=req_id)
            except Order.DoesNotExist:
                raise CommandError('Request "%s" does not exist' % req_id)

            request.status = 'Completed'
            request.save()
            reqname = Order.objects.get(pk=req_id)
            self.stdout.write(
                 self.style.SUCCESS(
                            'Successfully closed request "%s"' % reqname
                 )
            )
