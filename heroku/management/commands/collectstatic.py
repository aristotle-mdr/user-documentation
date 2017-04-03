import os
import subprocess
from tempfile import mkdtemp

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from django.test import override_settings
import static_precompiler

class Command(BaseCommand):
    args = '<workgroup_id workgroup_id ...>'
    help = 'Compiles all staticfiles into '

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--noinput",
            default=False,
            action='store_true',
        )

    def handle(self, *args, **options):
        call_command('migrate', '--run-syncdb')
        call_command('compilestatic')
        call_command('base_collectstatic', '--noinput')
        print("Emptying Database")
        call_command('flush', '--noinput')
        print("Loading fixtures")
        call_command('loaddata', 'server/fixtures/iso_metadata.json')
        call_command('loaddata', 'server/fixtures/test_metadata.json')

        print('All done!')

