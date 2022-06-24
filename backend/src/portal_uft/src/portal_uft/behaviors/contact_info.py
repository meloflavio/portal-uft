from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from portal_uft import _
from portal_uft import validators
from zope import schema
from zope.interface import provider, invariant


@provider(IFormFieldProvider)
class IContactInfo(model.Schema):
    """Contact Information behavior."""

    model.fieldset("contact", label=_("Contact"), fields=["email", "extension"])
    email = Email(title=_("person_email", default="E-mail"), required=True)

    extension = schema.TextLine(
        title=_(
            "Extension",
        ),
        required=False,
    )

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        email = data.email
        if not (email and validators.is_valid_email(email)):
            raise validators.BadValue(
                f"The email {email} is not in the uft.edu.br domain."
            )

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        extension = data.extension
        if not (extension and validators.is_valid_extension(extension)):
            raise validators.BadValue(
                f"The extension {extension} is not valid."
            )
