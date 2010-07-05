from zope.interface import implements
from zope.app.folder import Folder
from interfaces import IContent

class Content(Folder):
    """ Base content
    """
    implements(IContent)
