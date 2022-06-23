"""Validators"""
import re


def isValidEmail(value: str) -> bool:
    """Check if email is from UFT"""
    return value.endswith("@uft.edu.br")


def isValidExtension(value: str) -> bool:
    """Check if extension is valid"""
    return re.match(r"^\d{4}$", value)
