from django.core.management.base import BaseCommand
from dnaorder.models import Submission
from django.utils import timezone

class Command(BaseCommand):
    help = 'Check submissions for validity.'

    def handle(self, *args, **options):
        self.stdout.write('Validate submissions')
        for s in Submission.objects.filter(status__isnull=False).order_by('-submitted'):
            try:
                errors = s.samplesheet.validate()
                if len(errors) > 0:
                    print "**************ERRORS******************"
                    print s
                    print errors
                    s.data['validation']={'errors':errors,'updated':timezone.now().isoformat()}
                    s.save()
                elif hasattr(s.data, 'validation'):
                    del s.data['validation']
                    s.save()
                    
            except Exception, e:
                print '********Validation encountered an exception*********'
                print s
                print e