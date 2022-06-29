from kitconcept import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

@provider(IVocabularyFactory)
def campus_vocabulary(context):
    """Vocabulary of Campus in the site."""
    terms = []
    results = api.content.find(portal_type="campus")
    for result in results:
        token = result.UID
        title = result.Title
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
