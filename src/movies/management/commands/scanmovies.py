# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from movies.models import Movie
import os
from mutagen.mp4 import MP4


class Command(BaseCommand):
    help = "re-scans the movie db"

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        if not args:
            args = list(args)
            args.append(os.path.abspath(os.path.expanduser('~/media/movies')))
        for filePath in args:
            self.scanFolder(filePath)

    def extractTag(self, media, tag):
        data = media.get(tag)
        if not data: return ''
        obj = data[0]
        if obj:
            return ''.join(obj)
        return ''


    def scanFolder(self, start):
        print('scan folder: ' + start)
        start = os.path.abspath(start)
        for root, dirnames, filenames in os.walk(start):
            for filename in filenames:
                if not filename[-3:] == 'm4v':
                    continue
                filepath = os.path.join(root, filename)
                folderpath = os.path.relpath(root, start)
                name = filename[0:-4]
                print('analyze: ' + filepath)
                try:
                    movie = MP4(filepath)
                except MP4NoHeaderError:
                    print('error reading: ' + filepath)
                    continue
                title = self.extractTag(movie, b'\xa9nam')
                year = self.extractTag(movie, b'\xa9day')
                genre = self.extractTag(movie, b'\xa9gen')
                cover_data = movie['covr'][0]
                cover = os.path.join(folderpath, 'cover.jpg')
                desc = self.extractTag(movie, b'desc')
                source = os.path.join(folderpath, filename)
                self.writeMeta(root, title, year, genre, filename, name, desc)
                self.writeCover(start, cover, cover_data)
                self.writeModel(root, title, year, genre, source, cover, desc)

    def writeMeta(self, root, title, year, genre, source, name, desc):
        text = open(os.path.join(root, name + '.txt'), 'w', encoding='utf-8')
        text.write('TITLE: ' + title + '\n')
        text.write('YEAR: ' + year + '\n')
        text.write('GENRE: ' + genre + '\n')
        text.write('SOURCE: ' + source + '\n')
        text.write('COVER: cover.jpg' + '\n')
        text.write('DESC: ' + desc + '\n')
        text.close()

    def writeCover(self, start, path, data):
        cover = open(os.path.join(start, path), 'bw')
        cover.write(data)
        cover.close()

    def writeModel(self, root, title, year, genre, source, cover, desc):
        obj = Movie()
        obj.title = title
        obj.year = year
        obj.genre = genre
        obj.source = source
        obj.cover = cover
        obj.description = desc
        obj.save()



