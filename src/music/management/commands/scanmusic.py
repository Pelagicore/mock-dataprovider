# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from music.models import Track
import os

from mutagenx.id3 import ID3, ID3NoHeaderError

albums = set()


class Command(BaseCommand):
    help = "re-scans the music db"

    def handle(self, *args, **options):
        Track.objects.all().delete()
        if not args:
            args = list(args)
            args.append(os.path.abspath(os.path.expanduser('~/media/music')))
        for dir in args:
            self.scanRoot(dir)

    def extractTag(self, media, tag):
        obj = media.get(tag)
        if obj:
            return ''.join(obj)
        return u''

    def scanRoot(self, start):
        start = os.path.abspath(start)
        print(start)
        for root, folders, filenames in os.walk(start):
            for filename in filenames:
                # filename = filename.encode('utf-8')
                if not filename[-4:] == '.mp3':
                    continue
                filepath = os.path.join(root, filename)
                name = filename[0:-4]
                folderpath = os.path.relpath(root, start)
                print(u'analyze: {0}'.format(filepath.encode('utf-8')))
                try:
                    audio = ID3(filepath)
                except ID3NoHeaderError:
                    print('error reading: ' + filepath)
                    continue

                audio.pprint()
                # import pdb; pdb.set_trace()
                title = self.extractTag(audio, 'TIT2')
                album = self.extractTag(audio, 'TALB')
                artist = self.extractTag(audio, 'TPE1')
                track = self.extractTag(audio, 'TRCK')
                source = os.path.join(folderpath, filename)

                apics = audio.getall('APIC')[:1]
                apic = None
                if len(apics):
                    apic = apics[0]
                coverName = ''
                if apic:
                    if apic.mime == 'image/jpeg':
                        coverName = 'cover.jpg'
                    elif apic.mime == 'image/png':
                        coverName = 'cover.png'
                    else:
                        print('unknown cover mime type: ' + mime)
                # else:
                #     import pdb;
                #
                #     pdb.set_trace()
                #     print('!!! NO COVER')

                cover = os.path.join(folderpath, coverName)
                album_id = '%s/%s' % (album, artist)
                if not album_id in albums:
                    albums.add(album_id)
                    if apic:  # save new cover
                        cover_data = apic.data
                        self.writeCover(root, coverName, cover_data)
                self.writeMeta(root, title, album, artist, track, cover, name, filename)
                self.writeModel(root, title, album, artist, track, cover, source)

    def writeMeta(self, root, title, album, artist, track, cover, name, filename):
        text = open(os.path.join(root, name + '.txt'), 'w', encoding='utf-8')
        text.write(u'SOURCE: ' + filename + '\n')
        text.write(u'TITLE: ' + title + '\n')
        text.write(u'ALBUM: ' + album + '\n')
        text.write(u'ARTIST: ' + artist + '\n')
        text.write(u'TRACK: ' + track + '\n')
        text.write(u'COVER: cover.png' + '\n')
        text.close()

    def writeCover(self, root, coverName, data):
        cover = open(os.path.join(root, coverName), 'bw')
        cover.write(data)
        cover.close()

    def writeModel(self, root, title, album, artist, track, cover, source):
        obj = Track()
        obj.title = title
        obj.album = album
        obj.artist = artist
        obj.track = track
        obj.source = source
        obj.cover = cover
        obj.save()



