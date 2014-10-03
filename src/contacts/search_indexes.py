import datetime
from haystack import indexes
# from haystack import site
from contacts.models import Contact

class ContactIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    given_name = indexes.CharField(model_attr='given_name')
    surname = indexes.CharField(model_attr='surname')

    def get_model(self):
        return Contact

    def index_queryset(self, using=None):
        qs = Contact.objects.all()
        return qs


# site.register(Contact, ContactIndex)
