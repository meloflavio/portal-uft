from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


VOCABULARY = "portal_uft.vocabulary.cities"


class TestIndustriesVocabulary(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]

    def test_vocabulary(self):
        vocab = api.vocabulary.get(VOCABULARY)

        items = [item for item in vocab]

        self.assertEqual(len(items), 3)

    def test_vocabulary_titles(self):
        vocab = api.vocabulary.get(VOCABULARY)

        items = [item.title for item in vocab]

        self.assertIn("Palmas", items)
        self.assertIn("Araguaína", items)
        self.assertIn("Gurupi", items)
