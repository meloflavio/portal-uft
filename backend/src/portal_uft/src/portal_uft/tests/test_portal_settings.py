"""Portal settings tests."""
from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING  # noqa: E501

import unittest


class TestPortalSettings(unittest.TestCase):
    """Test that Portal configuration is correctly done."""

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        super().setUp()
        self.portal = self.layer["portal"]

    def test_portal_title(self):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Portal da UFT"
        self.assertEqual(value, expected)

    def test_portal_timezone(self):
        """Test portal timezone."""
        value = api.portal.get_registry_record("plone.portal_timezone")
        notExpected = "America/Sao_Paulo"
        expected = "America/Araguaina"
        self.assertEqual(value, expected)
        self.assertNotEquals(value, notExpected)

    def test_portal_enabled_sitemap(self):
        """Test portal enabled sitemap."""
        value = api.portal.get_registry_record("plone.enable_sitemap")
        self.assertTrue(value)

    def test_portal_mail_name(self):
        """Test portal mail name."""
        value = api.portal.get_registry_record("plone.email_from_name")
        expected = "Portal da UFT"
        self.assertEquals(expected, value)

    def test_portal_mail_address(self):
        """Test portal mail address."""
        value = api.portal.get_registry_record("plone.email_from_address")
        expected = "naoresponder@dti.uft.edu.br"
        addressValue = api.portal.get_registry_record("plone.email_from_address")
        self.assertEquals(expected, value)
