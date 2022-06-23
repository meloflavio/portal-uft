"""Validators"""
from portal_uft import _
from zope.interface import Invalid

import re


class BadValue(Invalid):
    """Exception rised when a provider value is informed"""

    __doc__ = _("The value is not correct")


def isValidEmail(value: str) -> bool:
    """Check if email is from UFT"""
    return value.endswith("@uft.edu.br")


def isValidExtension(value: str) -> bool:
    """Check if extension is valid"""
    return re.match(r"^\d{4}$", value)
