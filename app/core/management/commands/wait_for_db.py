"""
Django command to wait for the databse to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2pError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **optios):
        pass
        # self.stdout.write('wating for database...')
        # db_up = False
        # while db_up is False:
        #     try:
        #         self.check(databases=['default'])
        #         db_up = True
        #     except (Psycopg2pError, OperationalError):
        #         self.stdout.write('Database unavailable, wating 1 second ...')
        #         time.sleep(1)

        # self.stdout.write(self.style.SUCCESS('Database available!'))
