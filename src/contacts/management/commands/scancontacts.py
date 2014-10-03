from django.core.management.base import BaseCommand
from contacts.models import Contact
import csv
import sys


class Command(BaseCommand):
    help = "re-scans the contacts db"

    def handle(self, *args, **options):
        Contact.objects.all().delete()
        if not args:
            args = list(args)
            args.append('data/names.csv')
        for filePath in args:
            self.readData(filePath)

    def readData(self, filePath):
        data = csv.DictReader(open(filePath , encoding='utf-8'))
        count = 0
        print('reading: %s' % filePath)
        for row in data:
            count += 1
            sys.stdout.write('.')
            sys.stdout.flush()
            contact = Contact()
            contact.given_name = row['GivenName']
            contact.surname = row['Surname']
            contact.street_address = row['StreetAddress']
            contact.city = row['City']
            contact.zip_code = row['ZipCode']
            contact.country = row['Country']
            contact.email_address = row['EmailAddress']
            contact.telephone_number = row['TelephoneNumber']
            contact.save()
        print('\nready: %d contacts read' % count)
