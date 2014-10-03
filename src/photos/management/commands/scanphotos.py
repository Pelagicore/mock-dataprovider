from django.core.management.base import BaseCommand
from photos.models import Photo
import os
from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)

class FixedOffsetTZ(tzinfo):
    """Fixed offset in minutes east from UTC."""

    def __init__(self, offset, name):
        self.__offset = timedelta(minutes = offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return ZERO

berlin_tz = FixedOffsetTZ(3, 'Berlin')


class Command(BaseCommand):
    help = "re-scans the photos db"

    def handle(self, *args, **options):
        Photo.objects.all().delete()
        if not args:
            args = list(args)
            args.append(os.path.abspath(os.path.expanduser('~/media/photos')))
        self.scanRoot(args[0])

    def scanRoot(self, start):
        start = os.path.abspath(start)

        for root, folders, filenames in os.walk(start):
            for filename in filenames:
                if not filename[-4:] == '.jpg':
                    continue
                filepath = os.path.join(root, filename)
                name = filename[0:-4]
                folderpath = os.path.relpath(root, start)
                print('analyze: ' + filepath)
                created = self.createdTime(filepath)
                source = os.path.join(folderpath, filename)
                self.writeMeta(root, name, created, filename, name)
                self.writeModel(root, name, created, source)

    def createdTime(self, filename):
        t = os.path.getmtime(filename)
        return datetime.fromtimestamp(t, berlin_tz)

    def writeMeta(self, root, title, timestamp, source, name):
        text = open(os.path.join(root, name+'.txt'), 'w', encoding='utf-8')
        text.write('SOURCE: ' + source  + '\n')
        text.write('TITLE: ' + title + '\n')
        text.write('CREATED: ' + timestamp.isoformat() + '\n')
        text.close()

    def writeModel(self, root, title, timestamp, source):
        obj = Photo()
        obj.title = title
        obj.timestamp = timestamp
        obj.source = source
        obj.save()
