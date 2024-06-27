from django.core.management.base import BaseCommand
from checkout.models import Order
from django.db.models import Count


class Command(BaseCommand):
    help = 'Delete duplicate orders with the same stripe_pid'

    def handle(self, *args, **kwargs):
        duplicate_stripe_pids = (
            Order.objects
            .values('stripe_pid')
            .annotate(count=Count('id'))
            .filter(count__gt=1)
        )

        for stripe_pid in duplicate_stripe_pids:
            orders = Order.objects.filter(stripe_pid=stripe_pid['stripe_pid'])
            latest_order = orders.latest('date_created')
            orders.exclude(id=latest_order.id).delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Deleted duplicate orders for stripe_pid '
                    f'{stripe_pid["stripe_pid"]}'
                )
            )
