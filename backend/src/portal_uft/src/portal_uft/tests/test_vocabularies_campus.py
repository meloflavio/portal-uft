from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


VOCABULARY = "portal_uft.vocabulary.campus"

class TestCampusVocabulary(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING
    portal_type = "campus"

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        fti = api.fti.get(self.portal_type)
        fti.global_allow = True
        api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Palmas",
            description="Campus da UFT em Palmas",
            city="palmas",
            email="palmas@uft.edu.br",
            extension="2022",
        )
        api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Araguaina",
            description="Campus da UFT em Araguaina",
            city="araguaina",
            email="araguaina@uft.edu.br",
            extension="2023",
        )

    def test_vocabulary(self):
        vocab = api.vocabulary.get(VOCABULARY)
        terms = [term for term in vocab]
        self.assertEqual(len(terms), 2)

    def test_vocabulary_titles(self):
        vocab = api.vocabulary.get(VOCABULARY)
        titles = [term.title for term in vocab]
        self.assertIn("Palmas", titles)
        self.assertIn("Araguaina", titles)
