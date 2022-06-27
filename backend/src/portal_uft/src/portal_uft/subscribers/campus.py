from kitconcept import api
from portal_uft import logger
from portal_uft.content.campus import Campus
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _create_group(obj: Campus):
    groupName = f"group_{obj.title}"
    if api.group.get(obj.title):
        return
    api.group.create(groupName, obj.title, obj.description)
    logger.info(f"Created group {obj.title}")


def _update_tags(obj: Campus):
    """Update tags on Campus object."""
    vocab = api.vocabulary.get("portal_uft.vocabulary.cities")
    tags = {x for x in obj.subject if not x.startswith("Campus:")}
    city = obj.city
    term = vocab.getTermByToken(city)
    tags.add(f"Campus: {term.title}")
    obj.subject = tuple(tags)


def modified(obj: Campus, event: ObjectModifiedEvent):
    """Post modification handler for Campus."""
    _update_tags(obj)


def added(obj: Campus, event: ObjectAddedEvent):
    """Post creation handler for Campus."""
    _update_tags(obj)
    _create_group(obj)
