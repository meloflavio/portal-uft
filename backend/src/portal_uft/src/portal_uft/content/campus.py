"""A Campus profile in the site."""
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from zope import schema
from zope.interface import implementer


class ICampus(Schema):
    """Schema of a campus profile."""

    title = schema.TextLine(title=_("campus_title", default="Name"), required=True)

    description = schema.Text(
        title=_("campus_description", default="Description"), required=False
    )

    city = schema.Choice(
        title=_(
            "City",
        ),
        vocabulary="portal_uft.vocabulary.cities",
        required=True,
    )


@implementer(ICampus)
class Campus(Container):
    """A campus profile in the site."""
