from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft.behaviors import contact_info
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


class ContactInfoBehaviorTest(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING

    BEHAVIOR = "portal-uft.contact_info"

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_footer(self):
        behavior = api.fti.get_behavior_registration(self.BEHAVIOR)
        self.assertEqual(
            behavior.marker,
            contact_info.IContactInfo,
        )

    def test_applied_in_person(self):
        portal_type = "person"
        behaviors = api.fti.behaviors_for_type(portal_type)
        self.assertIn(self.BEHAVIOR, behaviors)

    def test_applied_in_campus(self):
        portal_type = "campus"
        behaviors = api.fti.behaviors_for_type(portal_type)
        self.assertIn(self.BEHAVIOR, behaviors)
