from django.core.management.base import BaseCommand, CommandError

from students.models import Group


class Command(BaseCommand):
    help = 'Show list of groups and students in them.'

    def handle(self, *args, **options):
        try:
            for group in Group.objects.all():
                self.stdout.write('=== {0} ==='.format(group.name))
                if group.students.all():
                    for student in group.students.all():
                        self.stdout.write(student.full_name)
                else:
                    self.stdout.write('There no students in this group.')
        except Group.DoesNotExist:
            raise CommandError('Does not exist any groups.')
