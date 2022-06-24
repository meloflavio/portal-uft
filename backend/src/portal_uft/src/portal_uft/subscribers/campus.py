from portal_uft.content.campus import Campus
from zope.lifecycleevent import ObjectAddedEvent


def _update_tags(obj: Campus):
    """Update tags on Campus object."""
    tags = set(obj.subject)
    city = obj.city
    tags.add(f"Campus: {city}")
    obj.subject = tuple(tags)


def added(obj: Campus, event: ObjectAddedEvent):
    """Post creation handler for Campus."""
    _update_tags(obj)
