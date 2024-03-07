from django.core.management.base import BaseCommand
from .models import Reserve

class Command(BaseCommand):
    help = 'Initialize table numbers'

    def handle(self, *args, **options):
       Reserve.table_number = Reserve.table_number()
