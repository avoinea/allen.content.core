""" Base interface to for allen content interfaces
"""
from zope.app.folder.interfaces import IFolder

class IContent(IFolder):
    """ Use this interface for your custom content-types
    """
